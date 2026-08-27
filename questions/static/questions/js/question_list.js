/* Capture original DOM order on page load for reset restore */
const originalOrder = [...document.querySelectorAll('.question-card')];

let submitted = false;

function submitExam() {
    if (submitted) return;
    submitted = true;
    document.getElementById('submit-btn').disabled = true;

    let right = 0, wrong = 0;

    document.querySelectorAll('.question-card').forEach(card => {
        const id = card.id.replace('card-', '');
        const correct = card.dataset.correct.split(',').map(s => s.trim()).filter(Boolean);
        const radios = card.querySelectorAll(`input[type="radio"][name="q${id}"]`);
        const selected = [];

        radios.forEach(r => {
            if (r.checked) selected.push(r.value);
            r.disabled = true;
        });

        if (correct.length === 0) return;

        const isCorrect =
            selected.length === correct.length &&
            correct.every(c => selected.includes(c));

        isCorrect ? right++ : wrong++;

        selected.forEach(val => {
            const lbl = document.getElementById(`lbl-${id}-${val}`);
            if (lbl) lbl.classList.add(isCorrect ? 'correct' : 'wrong');
        });

        if (!isCorrect) {
            correct.forEach(val => {
                const lbl = document.getElementById(`lbl-${id}-${val}`);
                if (lbl) lbl.classList.add('correct');
            });
        }

        document.getElementById(`answer-${id}`).classList.add('visible');
    });

    document.getElementById('right-count').textContent = right;
    document.getElementById('wrong-count').textContent = wrong;

    const statusEl = document.getElementById('status-text');
    statusEl.classList.remove('status-pending', 'status-passed', 'status-failed');
    if (right >= 26) {
        statusEl.textContent = 'Passed';
        statusEl.classList.add('status-passed');
    } else {
        statusEl.textContent = 'Failed';
        statusEl.classList.add('status-failed');
    }
}

/* Restore original DOM order and reset all question state */
function resetAll() {
    submitted = false;
    document.getElementById('submit-btn').disabled = false;
    document.getElementById('right-count').textContent = '0';
    document.getElementById('wrong-count').textContent = '0';

    const statusEl = document.getElementById('status-text');
    statusEl.textContent = 'Pending';
    statusEl.classList.remove('status-passed', 'status-failed');
    statusEl.classList.add('status-pending');

    const container = document.querySelector('main');
    const empty = container.querySelector('.empty');

    originalOrder.forEach(card => container.appendChild(card));
    if (empty) container.appendChild(empty);

    document.querySelectorAll('.question-card').forEach((card, i) => {
        const id = card.id.replace('card-', '');
        card.querySelector('.q-number').textContent = i + 1;

        card.querySelectorAll('input[type="radio"]').forEach(r => {
            r.checked = false;
            r.disabled = false;
        });

        card.querySelectorAll('.option-label').forEach(lbl => {
            lbl.classList.remove('correct', 'wrong');
        });

        document.getElementById(`answer-${id}`).classList.remove('visible');
    });
}

function shuffleQuestions() {
    if (submitted) resetAll();

    const container = document.querySelector('main');
    const cards = [...container.querySelectorAll('.question-card')];

    /* Fisher-Yates in-place shuffle */
    for (let i = cards.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        container.insertBefore(cards[j], cards[i].nextSibling);
        [cards[i], cards[j]] = [cards[j], cards[i]];
    }

    container.querySelectorAll('.question-card').forEach((card, i) => {
        card.querySelector('.q-number').textContent = i + 1;
    });
}
