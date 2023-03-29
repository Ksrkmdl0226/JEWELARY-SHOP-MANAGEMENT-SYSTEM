// category table

$("#create").click(function (e) {

    if ($("#txtName1").val() == "") {
        alert("Please Enter Category");
        $("#txtName1").focus();
        return false;
    }
    if ($("#filePhoto").val() == "") {
        alert("Please Select Photo");
        $("#filePhoto").focus();
        return false;
    }


    let formData = new FormData();
    var lclFile = document.getElementById("filePhoto");
    lclFile1 = lclFile.files[0];
    formData.append("filePhoto", lclFile1);
    formData.append("txtName1", $("#txtName1").val());
    // formData.append("filePhoto", $("#filePhoto").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action","add");

    $.ajax({
        url: "/category_details/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (result) {
            alert("Category Details Added");
            location.reload();
        },
        error: function (request, error) {
            console.error(error);
        },
        complete: function () {
            $(".btn .spinner-border").hide();
            $("#btn_add").attr("disabled", false);
        },
    });

});

// data table creation
// $("#create").click(function (e)){
function getData() {

    let formData = new FormData();
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "getData");

    $.ajax({
        url: "/category_details/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
            console.log(response);

            for (let i = 0; i < response.length; i++) {
                let j = i + 1;
                let img = response[i].cat_image.substring(3);
                $("#tableData").append('<tr><td class="text-center align-center">' + j +
                    '</td><td style="display: none;" class="text-center">' + response[i].cat_id +
                    '</td><td><img height="200" width="300" src='+img+'></td><td class="text-center">' + response[i].cat_name +
                    '</td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-toggle="modal" data-bs-target="#edit_modal" class="text-primary" onClick="getRowsUpdate();"> <i class="fas fa-pen"></i></a><a href="javascript:void(0);" title="Delete" data-toggle="modal" data-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();"> <i class="far fa-trash-alt"></i></a></div></td></tr>');
            }

            // $("#tableData").append('<tr></tr>');

        },
        error: function (request, error) {
            console.error(error);
        },
        complete: function () {
            $(".btn .spinner-border").hide();
            $("#btn_add").attr("disabled", false);
        },
    });
}
getData()


// update

$("#update").click(function (e) {

    if ($("#txtName2").val() == "") {
        alert("Please Enter Name");
        $("#txtName2").focus();
        return false;
    }

    if ($("#filePhoto1").val() == "") {
        alert("Please Select Photo");
        $("#filePhoto").focus();
        return false;
    }

    let formData = new FormData();
    formData.append("txtName2", $("#txtName2").val());
    // formData.append("txtPrice1", $("#txtPrice1").val());
    formData.append("id", $("#edit_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "update");

    $.ajax({
        url: "/category_details/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (result) {
            alert("Category Updated");
            location.reload();
        },
        error: function (request, error) {
            console.error(error);
        },
        complete: function () {
            $(".btn .spinner-border").hide();
            $("#btn_add").attr("disabled", false);
        },
    });

});


// Update()


function getRowsUpdate() {
    $("#tableData tr").click(function () {
        var currentRow = $(this).closest("tr");
        var lclID = currentRow.find("td:eq(1)").text();
        var lclName = currentRow.find("td:eq(2)").text();
        // alert(lclName);
        $("#txtName2").val(lclName);
        // $("#filePhoto1").val(filePhoto1);
        $("#edit_id").val(lclID);
        $('#edit_modal').modal('show');

    });
}



//delete data

function getRowsDelete() {
    $("#tableData tr").click(function () {
        var currentRow = $(this).closest("tr");
        var lclID = currentRow.find("td:eq(1)").text();
        // alert(lclID);
        $("#delete_id").val(lclID);
        $('#delete_modal').modal('show');


    });
}


$(document).on("click", "#btn_delete", function () {

    let formData = new FormData();
    formData.append("id", $("#delete_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "delete");

    // var table = $("#tableData").DataTable();

    $.ajax({
        beforeSend: function () {
            $(".btn .spinner-border").show();
        },

        url: "/category_details/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function () {
            alert("Product deleted succesfully");
            location.reload();
            table.ajax.reload();
            $("#delete_modal").modal('hide');
        },
        error: function (request, error) {
            console.error(error);
        },
        complete: function () {
            $(".btn .spinner-border").hide();
            $(".close").click();
        },
    });
});





