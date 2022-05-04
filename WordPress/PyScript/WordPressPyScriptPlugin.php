<?php
/**
 * Plugin Name:       WordPress PyScripter
 * Plugin URI:        https://raw.githubusercontent.com/TechnoCannon1337/Projects/master/WordPress/PyScript/WordPressPyScriptPlugin.php
 * Description:       The WordPress PyScripter plug in adds a link to the PyScript stylesheet and JavaScript source file to the head of your WordPress website and also deactivates the wptexturize functions to remove syntax errors resulting from modified quotation marks.
 * Version:           1.0
 * Requires at least: 5.9.3
 * Requires PHP:      5.9.3
 * Author:            Techno Cannon, MPA
 * Author URI:        https://technocannon.com/github
 * License:           GPL v2 or later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 * Update URI:        https://raw.githubusercontent.com/TechnoCannon1337/Projects/master/WordPress/PyScript/WordPressPyScriptPlugin.php
 */
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
