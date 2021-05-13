# `bulk-renamer`

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

* `add`: Adds a string in the name case based on the...
* `case`: Formats filename chars case based on the...
* `remove`: Remove a specified string from the filename.
* `replace`: Replaces a specified string in the filename...

## `br add`

Adds a string in the name case based on the subcommands.

**Usage**:

```console
$ br add [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `prefix`: Adds a string to the beginning of the...
* `suffix`: Adds a string to the ending of the filename.

### `br add prefix`

Adds a string to the beginning of the filename.

**Usage**:

```console
$ br add prefix [OPTIONS] VALUE
```

**Arguments**:

* `VALUE`: The string to be added to the beginning of the filename.  [required]

**Options**:

* `--help`: Show this message and exit.

### `br add suffix`

Adds a string to the ending of the filename.

**Usage**:

```console
$ br add suffix [OPTIONS] VALUE
```

**Arguments**:

* `VALUE`: The string to be added to the ending of the filename.  [required]

**Options**:

* `--help`: Show this message and exit.

## `br case`

Formats filename chars case based on the subcommands.

**Usage**:

```console
$ br case [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `alternate`: Alternate the name characters between upper...
* `camel`: Format the filename to camel case convention.
* `kebab`: Format the filename to kebab case convention.
* `lower`: Set the filename to lowercase.
* `pascal`: Format the filename to pascal case...
* `snake`: Format the filename to snake case convention.
* `upper`: Set the filename to uppercase.

### `br case alternate`

Alternate the name characters between upper and lowercase.

**Usage**:

```console
$ br case alternate [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `br case camel`

Format the filename to camel case convention.

**Usage**:

```console
$ br case camel [OPTIONS]
```

**Options**:

* `-w, --whitespace`: Maintains the filename whitespaces.  [default: False]
* `--help`: Show this message and exit.

### `br case kebab`

Format the filename to kebab case convention.

**Usage**:

```console
$ br case kebab [OPTIONS]
```

**Options**:

* `-u, --upper`: Set all characters to uppercase.  [default: False]
* `--help`: Show this message and exit.

### `br case lower`

Set the filename to lowercase.

**Usage**:

```console
$ br case lower [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `br case pascal`

Format the filename to pascal case convention.

**Usage**:

```console
$ br case pascal [OPTIONS]
```

**Options**:

* `-w, --whitespace`: Maintains the filename whitespaces.  [default: False]
* `--help`: Show this message and exit.

### `br case snake`

Format the filename to snake case convention.

**Usage**:

```console
$ br case snake [OPTIONS]
```

**Options**:

* `-u, --upper`: Set all characters to uppercase.  [default: False]
* `--help`: Show this message and exit.

### `br case upper`

Set the filename to uppercase.

**Usage**:

```console
$ br case upper [OPTIONS]
```

**Options**:

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
$ br replace [OPTIONS] OLD_VALUE NEW_VALUE
```

**Arguments**:

* `OLD_VALUE`: The string to shearch for.  [required]
* `NEW_VALUE`: The string to replace the old value with.  [required]

**Options**:

* `--help`: Show this message and exit.
