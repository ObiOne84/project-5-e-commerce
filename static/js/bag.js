$(document).ready(function () {
    // Source: Boutique Ado walkthrough project
    // Update quantity on click
    $('.update-item').click(function (e) {
        e.preventDefault();
        var qtyInputVal = parseInt($(this).closest('.table-row').find('.qty_input').val());
        var productTitle = $(this).closest('.table-row').find('.qty_input').data('product_title');
        var itemId = $(this).closest('.table-row').find('.qty_input').data('item_id');
        var $errorDiv = $('#input-error-' + itemId);
        if (qtyInputVal > 0 && qtyInputVal < 11) {
            var form = $(this).closest('.table-row').find('.update-form');
            form.submit();
        } else {
            $errorDiv.text(`You are attempting to add ${qtyInputVal} units of ${productTitle}. You can choose max 10 and min 1 product.`).removeClass('d-none');
            setTimeout(function () {
                $('.input-error').addClass('d-none');
            }, 15000);
        }
    });

    // Remove item and reload on click
    $('.remove-item').click(function (e) {
        e.preventDefault();
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
        var itemId = $(this).attr('id').split('remove_')[1];
        var url = `/bag/remove/${itemId}/`;

        // Send POST request to remove item
        $.post(url, {
                csrfmiddlewaretoken: csrfToken
            })
            .done(function () {
                location.reload();
            })
            .fail(function () {
                console.error('Failed to remove item.');
            });
    });
})