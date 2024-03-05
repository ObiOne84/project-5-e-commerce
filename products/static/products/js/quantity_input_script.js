// Source: Boutique Ado walkthrough project
$(document).ready(function () {
    // Disable +/- buttons outside 1-9 range
    function handleEnableDisable(itemId) {
        var currentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = currentValue < 2;
        var plusDisabled = currentValue > 9;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
        console.log(currentValue);
    }

    // Ensure proper enabling/disabling of all inputs on page load
    var allQtyInput = $('.qty_input');
    for (var i = 0; i < allQtyInput.length; i++) {
        var itemId = $(allQtyInput[i]).data('item_id');
        handleEnableDisable(itemId);
    }
    console.log(allQtyInput);

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        handleEnableDisable(itemId);
    });

    // Increment quantity
    $('.increment-qty').click(function(e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.qty_input');
        var itemId = $(closestInput).data('item_id');
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue + 1);
        handleEnableDisable(itemId);
        // console.log(closestInput);
        // console.log(itemId);
        // console.log(currentValue);
    });

    // Decrement quantity
    $('.decrement-qty').click(function(e) {
        e.preventDefault();
        var closestInput = $(this).closest('.input-group').find('.qty_input');
        var itemId = $(closestInput).data('item_id');
        var currentValue = parseInt($(closestInput).val());
        $(closestInput).val(currentValue - 1);
        handleEnableDisable(itemId);
        // console.log(closestInput);
        // console.log(itemId);
        // console.log(currentValue);
    });
});
