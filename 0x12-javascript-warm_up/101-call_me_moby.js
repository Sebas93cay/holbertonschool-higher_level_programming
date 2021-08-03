#!/usr/bin/node

const emparedado = function(n, f) {
  for (let i = 0; i < n; i++) {
    f();
  }
};
exports.callMeMoby = emparedado;
