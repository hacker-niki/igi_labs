function showPreloader() {
    $('.preloader').fadeIn('slow');
}

// Function to hide the preloader
function hidePreloader() {
    $('.preloader').fadeOut('slow');
}

// Функция для обновления отображения корзины
function updateCart() {
    $.ajax({
        url: "/get_small_cart",
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            console.log('cart-updated');
            console.log(Number(data['count']));
            document.getElementById('cart_num').innerHTML = data['count'];
        }
    });
}


function openTab(tabNo) {
    let HTML = "";
    try {
        for (let index = 0; index < tabData.length; ++index) {
            if (tabData[index]['ID']) {
                HTML += `
                    <tr class="d-lg-table-row fs-5">
                        <td class='text text-info '>${tabData[index]['ID']}</td>
                        <td class="text">${tabData[index]['Name']}</td>
                        <td class="text">${tabData[index]['Cost']}</td>
                        <td class="text">
                            <a href="#" class="btn btn-circle btn-sm btn-primary btn-sm add-to-cart" data="${tabData[index]['ID']}">
                                <i class="fa fa-cart-plus fs-6"></i>
                            </a>
                        </td>
                    </tr>`;
            } else {
                HTML += `<tr class="table-primary">
                        <th class="modal-title text-center" colSpan="4"><h3>${tabData[index]['Name']}</h3></th>
                    </tr>`
            }
        }
    } catch {
        HTML = "ERROR";
    }
    let elem = document.getElementById('tabContent');
    elem.innerHTML = HTML;
    hidePreloader();
    let tab = document.getElementById("tabContent")
    let elements = tab.querySelectorAll('a.add-to-cart');
    for (let index = 0; index < elements.length; ++index) {
        let element = elements[index];

        element.addEventListener("click", function (event) {

            $('#cart_nav').addClass('bitEffect');
            setTimeout(function () {
                $('#cart_nav').removeClass('bitEffect');
            }, 800);

            $.ajax({
                url: "/add_to_cart",
                type: "post",
                data: {productId: element.getAttribute('data')},
                success: function () {
                    updateCart();
                },
                error: function (error) {
                    alert("Ошибка при отправке данных");
                    console.error("Ошибка при отправке данных: ", error);
                },
            });

            event.preventDefault();
        });
    }
}

function getTab(tabNo) {
    showPreloader();
    $.ajax({
        url: "/get_price",
        type: 'GET',
        dataType: 'json',
        data: {tab: tabNo}, // Pass the tab number as a query parameter
        success: function (data) {
            tabData = data;
            openTab(tabNo); // Display the tab content after data is loaded
        },
        error: function () {
            // Handle error if data cannot be loaded
            tabData = []; // Set an empty array for this tab to avoid further requests
            openTab(tabNo); // Display the "No data available" message
        }
    });
}


// Обработчик события для кнопки "Купить"
function addToCart(productID) {
    $.ajax({
        url: "/add_to_cart",
        type: "post",
        data: {productId: productID},
        success: function (data) {
            // Обработка успешного ответа сервера
            console.log("Product added to cart");

            let dataParsed = JSON.stringify(data);
            const obj = JSON.parse(dataParsed);
            answer = obj.quantity;
            document.getElementById("count-" + productID).value = Number(answer);

            console.log("count updated");
            // Обновление содержимого корзины
        },
        error: function (error) {
            alert("Ошибка при отправке данных");
            console.error("Ошибка при отправке данных: ", error);
        },
    });
    updateCart();
}

function sendCart(formData) {
    $.ajax({
        url: "/send-cart",
        type: "POST",
        data: formData,
        success: function (response) {
            // Обработка успешного ответа сервера (если требуется)
            console.log("Message sent");
            // Перенаправление на другую страницу
            window.location.href = "/thanks";
        },
        error: function (xhr, status, error) {
            // Обработка ошибки (если требуется)
            console.error(error);
        }
    });
}

function removeFromCart(productID) {
    var answer = ''
    $.ajax({
        url: "/remove_from_cart",
        type: "POST",
        data: {product_id: productID},
        success: function (data) {
            // Обработка успешного ответа сервера
            console.log("Product removed from cart");
            let dataParsed = JSON.stringify(data);
            const obj = JSON.parse(dataParsed);
            answer = obj.quantity;
            document.getElementById("count-" + productID).value = Number(answer);
        },
        error: function (xhr, status, error) {
            // Обработка ошибки (если требуется)
            console.error(error);
        }
    });
}