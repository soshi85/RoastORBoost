// ===== Upload Page Logic =====
const fileInput = document.getElementById('file-input');
const dropZone = document.getElementById('drop-zone');
const fileInfo = document.getElementById('file-info');
const fileName = document.getElementById('file-name');
const fileSize = document.getElementById('file-size');
const removeBtn = document.getElementById('remove-file');
const submitBtn = document.getElementById('submit-btn');
const errorMessage = document.getElementById('error-message');
const loading = document.getElementById('loading');
const loadingText = document.getElementById('loading-text');
const fileSelection = document.getElementById('file-selection');

let selectedFile = null;

const MAX_SIZE = 5 * 1024 * 1024; // 5MB

const loadingMessages = [
    'در حال پیدا کردن دروغ‌های رزومه‌ات...',
    'داریم به Word و Excel می‌خندیم...',
    'سه پیشنهاد جدی آماده می‌شود...',
    'AI داره به رزومه‌ات نگاه می‌کنه...',
];

if (fileInput) {
    // انتخاب فایل با کلیک
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFile(e.target.files[0]);
        }
    });

    // Drag & Drop
    ['dragenter', 'dragover'].forEach(evt => {
        dropZone.addEventListener(evt, (e) => {
            e.preventDefault();
            dropZone.classList.add('dragover');
        });
    });

    ['dragleave', 'drop'].forEach(evt => {
        dropZone.addEventListener(evt, (e) => {
            e.preventDefault();
            dropZone.classList.remove('dragover');
        });
    });

    dropZone.addEventListener('drop', (e) => {
        const files = e.dataTransfer.files;
        if (files.length > 0) handleFile(files[0]);
    });

    removeBtn.addEventListener('click', () => {
        selectedFile = null;
        fileInput.value = '';
        fileInfo.hidden = true;
        dropZone.hidden = false;
        submitBtn.disabled = true;
        errorMessage.hidden = true;
    });

    submitBtn.addEventListener('click', () => {
        if (selectedFile) uploadResume(selectedFile);
    });
}

function handleFile(file) {
    errorMessage.hidden = true;

    if (file.type !== 'application/pdf' && !file.name.endsWith('.pdf')) {
        showError('فقط فایل PDF مجاز است.');
        return;
    }

    if (file.size > MAX_SIZE) {
        showError('حجم فایل بیشتر از ۵ مگابایت است.');
        return;
    }

    selectedFile = file;
    fileName.textContent = file.name;
    fileSize.textContent = formatSize(file.size);
    fileInfo.hidden = false;
    dropZone.hidden = true;
    submitBtn.disabled = false;
}

function showError(msg) {
    errorMessage.textContent = msg;
    errorMessage.hidden = false;
}

function formatSize(bytes) {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
}

async function uploadResume(file) {
    fileSelection.hidden = true;
    loading.hidden = false;

    let msgIndex = 0;
    const interval = setInterval(() => {
        msgIndex = (msgIndex + 1) % loadingMessages.length;
        loadingText.textContent = loadingMessages[msgIndex];
    }, 2500);

    try {
        await new Promise(resolve => setTimeout(resolve, 4000));
        const mockData = await fetch('samples/mock-success.json').then(r => r.json());

        localStorage.setItem('roastBoostResult', JSON.stringify(mockData));
        window.location.href = 'result.html';

    } catch (err) {
        clearInterval(interval);
        loading.hidden = true;
        fileSelection.hidden = false;
        showError('خطا در پردازش: ' + err.message);
    } finally {
        clearInterval(interval);
    }
}

const roastTextEl = document.getElementById('roast-text');
const boostListEl = document.getElementById('boost-list');
const shareBtn = document.getElementById('share-btn');

if (roastTextEl) {
    const stored = localStorage.getItem('roastBoostResult');

    if (!stored) {
        window.location.href = 'index.html';
    } else {
        const result = JSON.parse(stored);
        renderResult(result);
    }

    if (shareBtn) {
        shareBtn.addEventListener('click', () => {
            alert('قابلیت اشتراک‌گذاری در نسخه بعدی اضافه می‌شود! 🚀');
        });
    }
}

function renderResult(result) {
    const data = result.data || result;

    roastTextEl.textContent = data.roast_text || 'نقدی یافت نشد.';

    boostListEl.innerHTML = '';
    if (Array.isArray(data.boost_tips)) {
        data.boost_tips.forEach(tip => {
            const li = document.createElement('li');
            li.textContent = tip;
            boostListEl.appendChild(li);
        });
    }
}

function renderError(message) {
    roastTextEl.textContent = message;
    boostListEl.innerHTML = '';
}