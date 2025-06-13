pkgname=minish
pkgver=0.1.0
pkgrel=1
pkgdesc="A minimal custom linux shell written in Python"
arch=('x86_64')
url="https://github.com/jrifuoue/minish"
license=('GPLv2')
depends=('python')
source=("https://raw.githubusercontent.com/jrifuoue/minish/v${pkgver}/minish.py")
sha256sums=('SKIP')

build() {
    cp "${srcdir}/minish.py" "${srcdir}/minish"
    chmod +x "${srcdir}/minish"
}

package() {
    install -Dm755 "${srcdir}/minish" "${pkgdir}/usr/bin/minish"
}
