/// <reference path="jquery-1.10.2.intellisense.js" />
/// <reference path="jquery-1.10.2.min.js" />


var Download = Download || {}

var root = window.location;
var urls = {
    downloadfile: 'downloadfile/'
}

Download.downloadFile = function (contaid) {

    console.log(root + urls.downloadfile + String(contaid))

    $.ajax({
        url: root + urls.downloadfile + String(contaid),
        type: "GET",
        //data: { id: menuId },
    }).error(function () {
        alert("Desculpe, mas o download não pode ser feito!");
    });

}