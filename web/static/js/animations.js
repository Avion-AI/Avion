// Matrix Background Animation
function createMatrix() {
    const matrix = document.getElementById('matrix');
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    
    function createColumn() {
        const column = document.createElement('div');
        column.style.position = 'absolute';
        column.style.top = '-20px';
        column.style.left = Math.random() * 100 + '%';
        column.style.transform = 'translateX(-50%)';
        column.style.whiteSpace = 'nowrap';
        column.style.color = 'var(--accent)';
        column.style.fontFamily = 'var(--font-mono)';
        
        let content = '';
        for(let i = 0; i < 20; i++) {
            content += characters[Math.floor(Math.random() * characters.length)] + '<br>';
        }
        column.innerHTML = content;
        
        matrix.appendChild(column);
        
        let pos = -20;
        const interval = setInterval(() => {
            pos += 1;
            column.style.top = pos + 'px';
            if(pos > window.innerHeight) {
                clearInterval(interval);
                matrix.removeChild(column);
            }
        }, 50);
    }

    setInterval(createColumn, 500);
}

// Hover Effects
function initializeHoverEffects() {
    const buttons = document.querySelectorAll('.button');
    
    buttons.forEach(button => {
        button.addEventListener('mouseover', () => {
            button.style.transform = 'translateY(-2px)';
        });
        
        button.addEventListener('mouseout', () => {
            button.style.transform = 'translateY(0)';
        });
    });
}

// Initialize Animations
document.addEventListener('DOMContentLoaded', () => {
    createMatrix();
    initializeHoverEffects();
}); 