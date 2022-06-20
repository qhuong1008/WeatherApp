
function warning() {
    console.log('Vui long nhap du thong tin!')
}

function loadView() {
    var sel = document.getElementById('mydropdown') // find the drop down
    for (i = 1; i <= 50; i++) { // loop through all elements
      var opt = document.createElement("option"); // Create the new element
      opt.value = i; // set the value
      opt.text = i; // set the text
      sel.appendChild(opt); // add it to the select
    }
  }
  
  /*When an item is selcted from ComboBox*/
function comboItemselect(item) {
    var selectedItem = item.options[item.selectedIndex];
    // alert("selected item is : " + selectedItem.value);
    if(selectedItem.value == 1) {
        window.location.href = 'angiang';
    }
    if(selectedItem.value == 2) {
        window.location.href = 'brvt';
    }
    if(selectedItem.value == 3) {
        window.location.href = 'bacgiang';
    }
    if(selectedItem.value == 4) {
        window.location.href = 'backan';
    }
    if(selectedItem.value == 5) {
        window.location.href = 'baclieu';
    }
    if(selectedItem.value == 6) {
        window.location.href = 'bacninh';
    }
    if(selectedItem.value == 7) {
        window.location.href = 'bentre';
    }
    if(selectedItem.value == 8) {
        window.location.href = 'binhdinh';
    }
    if(selectedItem.value == 9) {
        window.location.href = 'binhduong';
    }
    if(selectedItem.value == 10) {
        window.location.href = 'binhphuoc';
    }
    if(selectedItem.value == 11) {
        window.location.href = 'binhthuan';
    }
    if(selectedItem.value == 12) {
        window.location.href = 'camau';
    }
    if(selectedItem.value == 13) {
        window.location.href = 'cantho';
    }
    if(selectedItem.value == 14) {
        window.location.href = 'caobang';
    }
    if(selectedItem.value == 15) {
        window.location.href = 'danang';
    }
    if(selectedItem.value == 16) {
        window.location.href = 'daklak';
    }
    if(selectedItem.value == 17) {
        window.location.href = 'daknong';
    }
    if(selectedItem.value == 18) {
        window.location.href = 'dienbien';
    }
    if(selectedItem.value == 19) {
        window.location.href = 'dongnai';
    }
    if(selectedItem.value == 20) {
        window.location.href = 'dongthap';
    }   
    if(selectedItem.value == 21) {
        window.location.href = 'gialai';
    }
    if(selectedItem.value == 22) {
        window.location.href = 'hagiang';
    }
    if(selectedItem.value == 23) {
        window.location.href = 'hanam';
    }
    if(selectedItem.value == 24) {
        window.location.href = 'hanoi';
    }
    if(selectedItem.value == 25) {
        window.location.href = 'hatinh';
    }
    if(selectedItem.value == 26) {
        window.location.href = 'haiduong';
    }
    if(selectedItem.value == 27) {
        window.location.href = 'haiphong';
    }
    if(selectedItem.value == 28) {
        window.location.href = 'haugiang';
    }
    if(selectedItem.value == 29) {
        window.location.href = 'hoabinh';
    }
    if(selectedItem.value == 30) {
        window.location.href = 'hungyen';
    }
    if(selectedItem.value == 31) {
        window.location.href = 'khanhhoa';
    }
    if(selectedItem.value == 32) {
        window.location.href = 'kiengiang';
    }
    if(selectedItem.value == 33) {
        window.location.href = 'kontum';
    }
    if(selectedItem.value == 34) {
        window.location.href = 'laichau';
    }
    if(selectedItem.value == 35) {
        window.location.href = 'lamdong';
    }
    if(selectedItem.value == 36) {
        window.location.href = 'langson';
    }
    if(selectedItem.value == 37) {
        window.location.href = 'laocai';
    }
    if(selectedItem.value == 38) {
        window.location.href = 'longan';
    }
    if(selectedItem.value == 39) {
        window.location.href = 'namdinh';
    }
    if(selectedItem.value == 40) {
        window.location.href = 'nghean';
    }
    if(selectedItem.value == 41) {
        window.location.href = 'ninhbinh';
    }
    if(selectedItem.value == 42) {
        window.location.href = 'ninhthuan';
    }
    if(selectedItem.value == 43) {
        window.location.href = 'phutho';
    }
    if(selectedItem.value == 44) {
        window.location.href = 'phuyen';
    }
    if(selectedItem.value == 45) {
        window.location.href = 'quangbinh';
    }
    if(selectedItem.value == 46) {
        window.location.href = 'quangnam';
    }
    if(selectedItem.value == 47) {
        window.location.href = 'quangngai';
    }
    if(selectedItem.value == 48) {
        window.location.href = 'quangninh';
    }
    if(selectedItem.value == 49) {
        window.location.href = 'quangtri';
    }
    if(selectedItem.value == 50) {
        window.location.href = 'soctrang';
    }
    if(selectedItem.value == 51) {
        window.location.href = 'sonla';
    }
    if(selectedItem.value == 52) {
        window.location.href = 'tayninh';
    }
    if(selectedItem.value == 53) {
        window.location.href = 'thaibinh';
    }
    if(selectedItem.value == 54) {
        window.location.href = 'thainguyen';
    }
    if(selectedItem.value == 55) {
        window.location.href = 'thanhhoa';
    }
    if(selectedItem.value == 56) {
        window.location.href = 'thuathienhue';
    }
    if(selectedItem.value == 57) {
        window.location.href = 'tiengiang';
    }
    if(selectedItem.value == 58) {
        window.location.href = 'hcm';
    }
    if(selectedItem.value == 59) {
        window.location.href = 'travinh';
    }
    if(selectedItem.value == 60) {
        window.location.href = 'tuyenquang';
    }
    if(selectedItem.value == 61) {
        window.location.href = 'vinhlong';
    }
    if(selectedItem.value == 62) {
        window.location.href = 'vinhphuc';
    }
    if(selectedItem.value == 63) {
        window.location.href = 'yenbai';
    }


}

function comboItemThongKeselect(item) {
    var selectedItem = item.options[item.selectedIndex];

    if(selectedItem.value == 1) {
        window.location.href = 'theothang_brunei';
    }
    if(selectedItem.value == 2) {
        window.location.href = 'theothang_cambodia';
    }
    if(selectedItem.value == 3) {
        window.location.href = 'theothang_indonesia';
    }
    if(selectedItem.value == 4) {
        window.location.href = 'theothang_laos';
    }
    if(selectedItem.value == 5) {
        window.location.href = 'theothang_malaysia';
    }
    if(selectedItem.value == 6) {
        window.location.href = 'theothang_myanmar';
    }
    if(selectedItem.value == 7) {
        window.location.href = 'theothang_philippines';
    }
    if(selectedItem.value == 8) {
        window.location.href = 'theothang_singapore';
    }
    if(selectedItem.value == 9) {
        window.location.href = 'theothang_thailand';
    }
    if(selectedItem.value == 10) {
        window.location.href = 'theothang_timoleste';
    }
    if(selectedItem.value == 11) {
        window.location.href = 'theothang_vietnam';
    }
}

function comboItemThongKeTBselect(item) {
    var selectedItem = item.options[item.selectedIndex];

    if(selectedItem.value == 'BRUNEI') {
        window.location.href = 'theothang_TB_brunei';
    }
    if(selectedItem.value == 'CAMBODIA') {
        window.location.href = 'theothang_TB_cambodia';
    }
    if(selectedItem.value == 'INDONESIA') {
        window.location.href = 'theothang_TB_indonesia';
    }
    if(selectedItem.value == 'LAOS') {
        window.location.href = 'theothang_TB_laos';
    }
    if(selectedItem.value == 'MALAYSIA') {
        window.location.href = 'theothang_TB_malaysia';
    }
    if(selectedItem.value == 'MYANMAR') {
        window.location.href = 'theothang_TB_myanmar';
    }
    if(selectedItem.value == 'PHILIPPINES') {
        window.location.href = 'theothang_TB_philippines';
    }
    if(selectedItem.value == 'SINGAPORE') {
        window.location.href = 'theothang_TB_singapore';
    }
    if(selectedItem.value == 'THAILAND') {
        window.location.href = 'theothang_TB_thailand';
    }
    if(selectedItem.value == 'TIMOLESTE') {
        window.location.href = 'theothang_TB_timoleste';
    }
    if(selectedItem.value == 'VIETNAM') {
        window.location.href = 'theothang_TB_vietnam';
    }
}

function xemchitiet() {
    // document.getElementById("brunei_temp_2m").style.color = "red";
    
}

function xulithongkejs() {
    window.location.href = 'xulithongke';
}

function xulicsvjs() {
    window.location.href = 'xemdulieu';
}


function comboTimeselect(item) {

}

function comboMonthselect(item) {
    
}

function comboYearselect(item) {

}

function comboTypeselect(item) {
    
}