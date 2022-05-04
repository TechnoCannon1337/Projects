<?php

function pyscript_head()
{
  ?>
  <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
  <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
  <?php

}


add_action( 'wp_head', 'pyscript_head' );
add_filter('run_wptexturize', '__return_false');
?>
