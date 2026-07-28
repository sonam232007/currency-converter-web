function swapCurrency() {

    let from = document.getElementsByName("from_currency")[0];
    let to = document.getElementsByName("to_currency")[0];

    let temp = from.value;
    from.value = to.value;
    to.value = temp;

}
