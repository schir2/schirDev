/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {

            colors: {
                'text-base': 'var(--text-base)',
                'text-muted': 'var(--text-muted)',
                'text-primary': 'var(--text-primary)',
                'text-secondary': 'var(--text-secondary)',
                'text-accent': 'var(--text-accent)',
                'text-error': 'var(--text-error)',
                'text-success': 'var(--text-success)',
                'text-link': 'var(--text-link)',

                'bg-base': 'var(--bg-base)',
                'bg-muted': 'var(--bg-muted)',
                'bg-primary': 'var(--bg-primary)',
                'bg-secondary': 'var(--bg-secondary)',
                'bg-accent': 'var(--bg-accent)',
                'bg-card': 'var(--bg-card)',
                'bg-overlay': 'var(--bg-overlay)',

                'border-base': 'var(--border-base)',
                'border-muted': 'var(--border-muted)',
                'border-primary': 'var(--border-primary)',
                'border-secondary': 'var(--border-secondary)',
                'border-accent': 'var(--border-accent)',
                'border-error': 'var(--border-error)',
                'border-success': 'var(--border-success)',

                'fill-base': 'var(--fill-base)',
                'fill-muted': 'var(--fill-muted)',
                'fill-primary': 'var(--fill-primary)',
                'fill-secondary': 'var(--fill-secondary)',
                'fill-accent': 'var(--fill-accent)',
                'fill-error': 'var(--fill-error)',
                'fill-success': 'var(--fill-success)',
            },
            transitionDuration: {
                '1500': '1500ms',
                '2000': '2000ms',
                '2500': '2500ms',
                '3000': '3000ms',
                // Add more durations as needed
            },
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
