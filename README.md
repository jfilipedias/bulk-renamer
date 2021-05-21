# bulk-renamer

Bulk Renamer is a CLI to help you to easily rename a
list of files. You just need to run the commands from the folder that contains
the files you want to rename.

**Usage**:

```console
$ br [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `alternate`: Alternate the name characters between upper and lowercase.
* `camel`: Format the filename to camel case convention.
* `kebab`: Format the filename to kebab case convention.
* `lower`: Set the filename to lowercase.
* `pascal`: Format the filename to pascal case convention.
* `prefix`: Adds a string to the beginning of the filename.
* `remove`: Remove a specified string from the filename.
* `replace`: Replaces a specified string in the filename with another specified string.
* `snake`: Format the filename to snake case convention.
* `suffix`: Adds a string to the ending of the filename.
* `upper`: Set the filename to uppercase.

## `br alternate`

Alternate the name characters between upper and lowercase.

**Usage**:

```console
$ br alternate [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `br camel`

Format the filename to camel case convention.

**Usage**:

```console
$ br camel [OPTIONS]
```

**Options**:

* `-w, --whitespace`: Maintains the filename whitespaces.  [default: False]
* `--help`: Show this message and exit.

## `br kebab`

Format the filename to kebab case convention.

**Usage**:

```console
$ br kebab [OPTIONS]
```

**Options**:

* `-u, --upper`: Set all characters to uppercase.  [default: False]
* `--help`: Show this message and exit.

## `br lower`

Set the filename to lowercase.

**Usage**:

```console
$ br lower [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `br pascal`

Format the filename to pascal case convention.

**Usage**:

```console
$ br pascal [OPTIONS]
```

**Options**:

* `-w, --whitespace`: Maintains the filename whitespaces.  [default: False]
* `--help`: Show this message and exit.

## `br prefix`

Adds a string to the beginning of the filename.

**Usage**:

```console
$ br prefix [OPTIONS]
```

**Options**:

* `--value TEXT`: The string to be added to the beginning of the filename.  [default: ]
* `--help`: Show this message and exit.

## `br remove`

Remove a specified string from the filename.

**Usage**:

```console
$ br remove [OPTIONS] VALUE
```

**Arguments**:

* `VALUE`: The string to remove from filename.  [required]

**Options**:

* `--help`: Show this message and exit.

## `br replace`

Replaces a specified string in the filename with another specified string.

**Usage**:

```console
$ br replace [OPTIONS]
```

**Options**:

* `--old-value TEXT`: The string to shearch for.  [default: ]
* `--new-value TEXT`: The string to replace the old value with.  [default: ]
* `--help`: Show this message and exit.

## `br snake`

Format the filename to snake case convention.

**Usage**:

```console
$ br snake [OPTIONS]
```

**Options**:

* `-u, --upper`: Set all characters to uppercase.  [default: False]
* `--help`: Show this message and exit.

## `br suffix`

Adds a string to the ending of the filename.

**Usage**:

```console
$ br suffix [OPTIONS]
```

**Options**:

* `--value TEXT`: The string to be added to the ending of the filename.  [default: ]
* `--help`: Show this message and exit.

## `br upper`

Set the filename to uppercase.

**Usage**:

```console
$ br upper [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
