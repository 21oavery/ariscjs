let worker = new Worker("comp.js");
worker.addEventListener("message", function() {
    alert(e.data);
});
