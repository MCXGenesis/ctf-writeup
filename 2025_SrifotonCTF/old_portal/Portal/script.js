function buatKodeRahasia() {
  let dataAwal = "dGhlcmVpc25vc2VjcmV0";
  
  let kodeFinal = atob(dataAwal).split('').reverse().join('');
  
  return kodeFinal;
}

function validasiKode() {
  let inputPengguna = document.getElementById('kode_akses').value;
  
  let kodeBenar = buatKodeRahasia();
  
  if (inputPengguna === kodeBenar) {
    let flagContainer = document.getElementById('hasil_flag');
    flagContainer.innerText = "Flag: LVZHSLCA{lp1w_z5_x0w_l3vvvv}\nSeorang diplomat Prancis dari abad ke-16 meninggalkan metode ini. Gunakan kunci yang telah kau dapatkan";
    
    document.getElementById('tombol_buka').disabled = false;
    document.getElementById('kode_akses').disabled = false;

  } else {
    alert("Kode Akses Salah!");
  }
}
