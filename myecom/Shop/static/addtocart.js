document.addEventListener("DOMContentLoaded", function () {
    let totalPrice = 0;


    document.querySelectorAll(".product-content h2").forEach(function (priceElement) {
        let priceText = priceElement.innerText.replace("Rs:", "").trim(); 
        let price = parseInt(priceText); 

        if (!isNaN(price)) {
            totalPrice += price; 
        }
    });

   
    let subtotalElement = document.querySelector(".side-container h2");
    if (subtotalElement) {
        subtotalElement.innerText = `Subtotal (items): Rs ${totalPrice}`;
    }
});
