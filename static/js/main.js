// Kemboi Developers - Premium Frontend JS

console.log('%c[Kemboi] Premium web app initialized successfully.', 'color:#166534');

document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Add subtle hover effects to project cards
    document.querySelectorAll('.project-card').forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-12px)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });
    
    // Toast notification system
    window.showToast = function(message, type = 'success') {
        const toast = document.createElement('div');
        toast.className = `fixed bottom-6 right-6 px-6 py-3 rounded-3xl shadow-xl text-sm font-medium flex items-center gap-x-3 z-[999] ${type === 'success' ? 'bg-emerald-600 text-white' : 'bg-red-600 text-white'}`;
        toast.innerHTML = `
            <div>${message}</div>
            <button onclick="this.parentElement.remove()" class="ml-3 text-xl leading-none">&times;</button>
        `;
        document.body.appendChild(toast);
        
        setTimeout(() => {
            if (toast.parentNode) toast.parentNode.removeChild(toast);
        }, 4800);
    };
});

// Real-time notifications (simulated)
function initRealtime() {
    setInterval(() => {
        const badge = document.querySelector('.notification-badge');
        if (badge) {
            badge.style.transform = 'scale(1.2)';
            setTimeout(() => {
                if (badge) badge.style.transform = 'scale(1)';
            }, 300);
        }
    }, 30000);
}

initRealtime();