<?php
/**
 * Plugin Name:       PyPlugger for PyScript
 * Plugin URI:        https://github.com/TechnoCannon1337/Projects/raw/master/WordPress/PyScript/PyPluggerforPyScript.zip
 * Description:       PyPlugger for PyScript adds a link to the PyScript stylesheet and JavaScript source file to the head and footer of your WordPress website and also deactivates the wptexturize functions to remove syntax errors resulting from modified quotation marks.
 * Version:           1.0
 * Requires at least: 5.9.3
 * Requires PHP:      7.0
 * Author:            Techno Cannon, MPA
 * Author URI:        https://technocannon.com/github
 * License:           GPL v2 or later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 */

function pyPluggerFix_1_0() {
  wp_enqueue_script('pyPlugger-Script-ID', 'https://pyscript.net/alpha/pyscript.js', array(), null, true);

  wp_enqueue_style('pPlugger-Style-ID', 'https://pyscript.net/alpha/pyscript.css', array(), null);

}

add_action( 'wp_enqueue_scripts', 'pyPluggerFix_1_0' );
add_filter('run_wptexturize', '__return_false');

?>
