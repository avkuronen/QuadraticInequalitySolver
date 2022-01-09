s_of = 'less;'
if (document.getElementById('isStrict').checked) {
    s_of += 'strict'
} else {
    s_of += 'not_strict'
}
document.getElementById('sign_of').value = s_of