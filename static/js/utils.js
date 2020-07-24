var custom = {
  "ce": (name, attributes={}, ...children) => {
    if (name == "__TEXT__") {return document.createTextNode(children[0] || "")}

    let element = name == "__FRAG__" ? new DocumentFragment() : document.createElement(name);
    for (var k of Object.keys(attributes)) {element.setAttribute(k, attributes[k])}
    children.forEach((child) => {element.appendChild(custom.ce(...child))});
    return element
  },
  "setCSS": (element, css) => {
    Object.entries(css).map(([k, v]) => {
      element.style.setProperty(k, v)
    });
  },
  "range": function* (start, stop, step=1) {
    if (!stop) {
      stop = start;
      start = 0;
    }

    if ((step > 0 && start >= stop) || (step < 0 && start <= stop)) {
      return [];
    }

    for (var i = start; step > 0 ? i < stop : i > stop; i += step) {
      yield i;
    }
  }
}
