<?php
function python_pyscript()
{
  wp_register_script('pythonpyscript', 'https://pyscript.net/alpha/pyscript.js', array(), false, false);
	wp_enqueue_script('pythonpyscript');

}

function pyscript_style()
{
	wp_enqueue_style('pyscriptstyle', 'https://pyscript.net/alpha/pyscript.css', array(), false, 'all');
}


add_action('wp_enqueue_scripts', 'pyscript_style');

add_action('wp_enqueue_scripts', 'python_pyscript');
