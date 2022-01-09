s_of = ''
if (document.getElementById('more').checked) {
    s_of += 'more;'
} else if (document.getElementById('less').checked) {
    s_of += 'less;'
}
if (document.getElementById('isStrict').checked) {
    document.getElementById('more_val').innerHTML = '> 0'
    document.getElementById('less_val').innerHTML = '< 0'
    s_of += 'strict'
} else {
    document.getElementById('more_val').innerHTML = '≥ 0'
    document.getElementById('less_val').innerHTML = '≤ 0'
    s_of += 'not_strict'
}
document.getElementById('sign_of').value = s_of