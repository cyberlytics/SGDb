<script lang="ts">
  export let id;
  /* fetch the data from the backend
  const { data, error } = await fetch(`/api/game/${id}`).then((r) => r.json());
  if (error) {
    console.error(error);
  }
  */
</script>

<!-- <p class="text-black">GAME {id}</p> -->
<!-- blue Backround-->
<div class="bg-blue-500">
  <p class="text-white">GAME {id}</p>
</div>

<!-- insert image by URL left and backround blue-->

<div class="bg-blue-500"> <!-- blue Backround-->
  <img
    src="https://s1.1zoom.me/big0/367/Call_of_Duty_Soldiers_475128.jpg"
    alt="image"
    class="w-1/2"
    style="float: left;"
    width="300"
    height="300"

  />
  <!--set table right to image-->
  <table class="w-1/2">
    <tr>
      <td>Game Name</td>
      <td>Counter Strike</td>
    </tr>
    <tr>
      <td>Developer</td>
      <td>Valve</td>
    </tr>
    <tr>
      <td>Release Date</td>
      <td>August 21, 1999</td>
    </tr>
    <tr>
      <td>Genre</td>
      <td>First-Person Shooter</td>
    </tr>
    <tr>
      <td>Platform</td>
      <td>PC</td>
    </tr>
    <tr>
      <td>Link zum Spiel</td>
      <td>
          <!-- Set hyperlink under table-->
          <a href="https://store.steampowered.com/app/10/CounterStrike/" class="w-1/2">Offizielle Webseite</a>
      </td>
    </tr>
  </table>

<!-- set descripton under table-->
<section class="w-1/2">

  <p class="text-white">
    Beschreibung:
  </p>
  <p class="text-white">
    Counter-Strike (CS) ist ein Computerspiel aus dem Genre der Online-Taktik-Shooter. Es wurde von Valve und Hidden Path Entertainment entwickelt und stellt das erste Spiel der Counter-Strike-Reihe dar. Das Spiel wurde am 21. August 1999 veröffentlicht und gilt als eines der erfolgreichsten Computerspiele überhaupt. Counter-Strike ist ein Mehrspieler-Online-Shooter, bei dem zwei Teams gegeneinander antreten. Das Spiel ist in der First-Person-Perspektive gehalten und wird über das Internet gespielt. Die Spieler können sich in die Rolle eines Terroristen oder eines Antiterrorkommandos versetzen. Ziel des Spiels ist es, die gegnerische Basis zu zerstören oder die gegnerischen Spieler zu töten. Das Spiel ist kostenlos und kann über Steam heruntergeladen werden.
  </p>
</section>
</div>

  

<!-- text black-->
<style>
  .text-black {
    color: #000;
  }
  .text-white {
    color: #fff;
  }
  .table, th, td {
      padding: 10px;
      border: 1px solid rgb(238, 239, 252); 
      border-collapse: collapse;
      }
</style>