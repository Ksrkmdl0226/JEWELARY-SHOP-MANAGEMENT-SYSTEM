$("#btn_add").click(function (e) {
  //verification
  if ($("#filePhoto").val() == "") {
    alert("Please Select Photo");
    $("#filePhoto").focus();
    return false;
  }

  if ($("#selType").val() == "") {
      alert("Please Select Type");
    $("#selType").focus();
    return false;
  }

  if ($("#txtName").val() == "") {
      alert("Please Enter Name");
    $("#txtName").focus();
    return false;
  }

  if ($("#txtWeight").val() == "") {
      alert("Please Enter Weight");
    $("#txtWeight").focus();
    return false;
  }

  if ($("#txtRate").val() == "") {
      alert("Please Enter Rate");
    $("#txtRate").focus();
    return false;
  }

  if ($("#txtDesc").val() == "") {
      alert("Please Enter Description");
    $("#txtDesc").focus();
    return false;
  }

  var formData = new FormData();

  var lclFile = document.getElementById("filePhoto");
  lclFile1 = lclFile.files[0];
  formData.append("filePhoto", lclFile1);
  formData.append("selType", $("#selType").val());
  formData.append("txtName", $("#txtName").val());
  formData.append("txtWeight", $("#txtWeight").val());
  formData.append("txtRate", $("#txtRate").val());
  formData.append("txtDesc", $("#txtDesc").val());
  formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
  formData.append("action", "add");

  // var table = $("#tableData").DataTable();

  $.ajax({
      url: "/product_details/",
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      success: function (result) {
          alert("Product Details Added");
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



function getData() {

var formData = new FormData();
formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
formData.append("action", "getData");

$.ajax({

    url: "/product_details/",
    type: "POST",
    data: formData,
    processData: false,
    contentType: false,
    success: function (response) {
      $("#tableData tr:gt(0)").remove();
      for(let i = 0; i < response.length; i++) {
        let j = i + 1;
        let img=response[i].ap_image.substring(3);
        $("#tableData").append('<tr><td>'+j+'</td><td style="display: none;">'+response[i].ap_id+'</td><td><img height="100" width="100" src='+img+'></td><td>'+response[i].ap_type+'</td><td>'+response[i].ap_name+'</td><td>'+response[i].ap_weight+'</td><td>'+response[i].ap_rate+'</td><td>'+response[i].ap_description+'</td><td><div class="d-flex" style="justify-content: space-evenly;"><a href="javascript:void(0);" id="edit_row" title="View/Edit" data-bs-toggle="modal" data-bs-target="#edit_modal" class="text-primary" onClick="getRowsUpdate();"> <i class="fas fa-pen"></i></a><a href="javascript:void(0);" title="Delete" data-bs-toggle="modal" data-bs-target="#delete_modal" class="text-danger" id="delete_row" onClick="getRowsDelete();"> <i class="far fa-trash-alt"></i></a></div></td></tr>');
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
  snackbar_error("Please Enter Name");
  $("#txtName1").focus();
  return false;
}

if ($("#selType1").val() == "") {
  snackbar_error("Please Select Type");
  $("#selType1").focus();
  return false;
}

if ($("#txtWeight1").val() == "") {
  snackbar_error("Please Enter Weight");
  $("#txtWeight1").focus();
  return false;
}

if ($("#txtRate1").val() == "") {
  snackbar_error("Please Enter Rate");
  $("#txtRate1").focus();
  return false;
}

if ($("#txtDesc1").val() == "") {
  snackbar_error("Please Enter Description");
  $("#txtDesc1").focus();
  return false;
}

var formData = new FormData()
formData.append("selType1", $("#selType1").val());
formData.append("txtName1", $("#txtName1").val());
formData.append("txtWeight1", $("#txtWeight1").val());
formData.append("txtRate1", $("#txtRate1").val());
formData.append("txtDesc1", $("#txtDesc1").val());
formData.append("id", $("#edit_id").val());
formData.append("csrfmiddlewaretoken", $('input[name=csrfmiddlewaretoken]').val());
formData.append("action", "update");

// var table = $("#tableData").DataTable();

$.ajax({
  beforeSend: function () {
    $(".btn .spinner-border").show();
    $("#btn_update").attr("disabled", true);
  },
  url: "/product_details/",
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
    var lclImage = currentRow.find("td:eq(2)").text();
    var lclType = currentRow.find("td:eq(3)").text();
    var lclName = currentRow.find("td:eq(4)").text();
    var lclWeight = currentRow.find("td:eq(5)").text();
    var lclRate = currentRow.find("td:eq(6)").text();
    var lclDesc = currentRow.find("td:eq(7)").text();

    // alert(lclType);
    $("#imgURL1").val(lclImage);
    $("#txtName1").val(lclName);
    $("#selType1").val(lclType);
    $("#txtWeight1").val(lclWeight);
    $("#txtRate1").val(lclRate);
    $("#txtDesc1").val(lclDesc);
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

  url: "/product_details/",
  type: "POST",
  data: formData,
  processData: false,
  contentType: false,
  success: function () {
    snackbar_success("Product deleted succesfully");
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



