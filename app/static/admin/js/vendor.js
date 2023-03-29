$("#btn_add").click(function (e) {
    //verification
    if ($("#txtName").val() == "") {
        alert("Please Enter Shop Name");
        $("#txtName").focus();
        return false;
    }

    if ($("#txtvenName").val() == "") {
        alert("Please Select Type");
        $("#txtvenName").focus();
        return false;
    }

    if ($("#txtcontact").val() == "") {
        alert("Please Enter Name");
        $("#txtcontact").focus();
        return false;
    }

    if ($("#txtemail").val() == "") {
        alert("Please Enter Weight");
        $("#txtemail").focus();
        return false;
    }

     if ($("#txtPassword").val() == "") {
        alert("Please Enter Password");
        $("#txtPassword").focus();
        return false;
    }

    const newLocal = "#selType";
    if ($(newLocal).val() == "") {
        alert("Please select Place");
        $("#selType").focus();
        return false;
    }



    var formData = new FormData();

    formData.append("txtName", $("#txtName").val());
    formData.append("txtvenName", $("#txtvenName").val());
    formData.append("txtcontact", $("#txtcontact").val());
    formData.append("txtemail", $("#txtemail").val());
    formData.append("txtPassword", $("#txtPassword").val());
    formData.append("selType", $("#selType").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "add");

    // var table = $("#tableData").DataTable();

    $.ajax({
        url: "/vendor_details/",
        type: "POST",
        data: formData,
        processData: false,
        contentType: false,
        success: function (result) {
            alert("Vendor Details Added");
            location.reload();
        },
        error: function (request, error) {
          console.error (error);
      },
        complete: function () {
            $(".btn .spinner-border").hide();
            $("#btn_add").attr("disabled", false);
        },
    });
});



function getData() {

  var formData = new FormData();
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "getData");

  $.ajax({

      url: "/vendor_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (response) {
          $("#tableData tr:gt(0)").remove();
          for (let i = 0; i < response.length; i++) {
              let j = i + 1;
              $("#tableData").append('<tr><td>' + j + '</td><td style="display: none;">'+ response[i].vend_id+'</td><td>'+ response[i].vend_shopname +'</td><td>' + response[i].vend_name + '</td><td>' + response[i].vend_contact + '</td><td>' + response[i].vend_email + '</td><td>' + response[i].vend_place + '</td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-bs-toggle="modal" data-bs-target="#edit_modal" class="text-primary" onClick="getRowsUpdate();"> <i class="fas fa-pen"></i></a><a href="javascript:void(0);" title="Delete" data-bs-toggle="modal" data-bs-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();"> <i class="far fa-trash-alt"></i></a></div></td></tr>');
          }
      },
      error: function (request, error) {
          console.error(error);
      },
      complete: function () {

      },
  });

}
getData()




// update modal of product
$("#btn_update").click (function(e) {

    if ($("#txtName1").val() == "") {
        alert("Please Enter Shop Name");
        $("#txtName1").focus();
        return false;
    }

    if ($("#txtvenName1").val() == "") {
        alert("Please Enter Vendor Name");
        $("#txtvenName1").focus();
        return false;
    }

    if ($("#txtcontact1").val() == "") {
        alert("Please Enter Contact No");
        $("#txtcontact1").focus();
        return false;
    }

    if ($("#txtemail1").val() == "") {
        alert("Please Enter Mail");
        $("#txtemail1").focus();
        return false;
    }

    const newLocal = "#selType1";
    if ($(newLocal).val() == "") {
        alert("Please select Place");
        $("#selType1").focus();
        return false;
    }
    
    var formData = new FormData()
    formData.append("txtName1", $("#txtName1").val());
    formData.append("txtvenName1", $("#txtvenName1").val());
    formData.append("txtcontact1", $("#txtcontact1").val());
    formData.append("txtemail1", $("#txtemail1").val());
    formData.append("selType1", $("#selType1").val());
    formData.append("id", $("#edit_id").val());
    formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
    formData.append("action", "update");
  
    // var table = $("#tableData").DataTable();
  
    $.ajax({
      beforeSend: function () {
        $(".btn .spinner-border").show();
        $("#btn_update").attr("disabled", true);
      },
      url: "/vendor_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
        alert("Product Details Updated Succesfully");
        location.reload();
        // table.ajax.reload();
        $("#edit_modal").modal('hide');
      },
      error: function (request, error) {
        console.error(error);
      },
      complete: function () {
        $(".btn .spinner-border").hide();
        $("#btn_update").attr("disabled", false);
      },
    });
  });
  
  
  
  // Update()
  
  function getRowsUpdate() {
    $("#tableData tr").click(function() {
        var currentRow = $(this).closest("tr");
        var lclID = currentRow.find("td:eq(1)").text();
        var lclName = currentRow.find("td:eq(2)").text();
        var lclVName = currentRow.find("td:eq(3)").text();
        var lclCon = currentRow.find("td:eq(4)").text();
        var lclMail = currentRow.find("td:eq(5)").text();
        var lclPlace = currentRow.find("td:eq(6)").text();
        
        // alert(lclType);
        $("#txtName1").val(lclName);
        $("#txtvenName1").val(lclVName);
        $("#txtcontact1").val(lclCon);
        $("#txtemail1").val(lclMail);
        $("#selType1").val(lclPlace);
        $("#edit_id").val(lclID);
         
    });
  }
  
  
  function getRowsDelete() {
    $("#tableData tr").click(function() {
        var currentRow = $(this).closest("tr");
        var lclID = currentRow.find("td:eq(1)").text();
        // alert(lclID);
        $("#delete_id").val(lclID);
  
    });
  }
  
 //Delete work step
$(document).on("click", "#btn_delete", function () {

  var formData = new FormData();
  formData.append("id", $("#delete_id").val());
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "delete");

  // var table = $("#tableData").DataTable();

  $.ajax({
    beforeSend: function () {
      $(".btn .spinner-border").show();
    },

    url: "/vendor_details/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function () {
      snackbar_success("Vendor deleted succesfully");
      location.reload();
      table.ajax.reload();
      $("#delete_modal").modal('hide');
    },
    error: function (request, error) {
      console.error(error);
    },
    complete: function () {
      $(".btn .spinner-border").hide();
      // Reset Form
      //$("#view_field_form")[0].reset();
      $(".close").click();
    },
  });
});






