(async () => {
    let start = performance.now();
    await awaiting(() => {
        return performance.now() - start > 5000;
    });
    finish('123');
})();