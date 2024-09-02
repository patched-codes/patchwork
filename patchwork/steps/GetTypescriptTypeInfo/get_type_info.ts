import fs from "fs";
import path from "path";
import {
  ClassDeclaration,
  EnumDeclaration,
  FunctionDeclaration,
  InterfaceDeclaration,
  Project,
  PropertyDeclaration,
  Type,
  TypeAliasDeclaration,
  VariableDeclaration,
} from "ts-morph";

class TypeInfo {
  private maxDepth: number;

  private project: Project;

  constructor(maxDepth: number) {
    this.maxDepth = maxDepth;
    this.project = new Project();
  }

  public describe(identifier: string, filePath: string): string {
    const sourceFile = this.project.addSourceFileAtPath(filePath);

    const classDeclaration = sourceFile.getClass(identifier);
    if (classDeclaration) {
      return this.describeClass(classDeclaration, 0);
    }

    const interfaceDeclaration = sourceFile.getInterface(identifier);
    if (interfaceDeclaration) {
      return this.describeInterface(interfaceDeclaration, 0);
    }

    const typeAlias = sourceFile.getTypeAlias(identifier);
    if (typeAlias) {
      return this.describeTypeAlias(typeAlias, 0);
    }

    const variable = sourceFile.getVariableDeclaration(identifier);
    if (variable) {
      return this.describeVariable(variable, 0);
    }

    const functionDeclaration = sourceFile.getFunction(identifier);
    if (functionDeclaration) {
      return this.describeFunction(functionDeclaration, 0);
    }

    const enumDeclaration = sourceFile.getEnum(identifier);
    if (enumDeclaration) {
      return this.describeEnum(enumDeclaration, 0);
    }

    throw new Error(`Identifier ${identifier} not found in ${filePath}`);
  }

  private describeVariable(
    variable: VariableDeclaration,
    depth: number
  ): string {
    if (depth > this.maxDepth) {
      return "";
    }
    const indent = "  ".repeat(depth);
    return `${indent}const ${variable.getName()}: ${this.describeType(
      variable.getType(),
      depth + 1
    )}`;
  }

  private describeFunction(
    functionDeclaration: FunctionDeclaration,
    depth: number
  ): string {
    if (depth > this.maxDepth) {
      return "";
    }
    const indent = "  ".repeat(depth);
    return `${indent}function ${functionDeclaration.getName()}(${functionDeclaration
      .getParameters()
      .map(
        (param) =>
          `${param.getName()}: ${this.describeType(param.getType(), depth + 1)}`
      )
      .join(", ")}): ${this.describeType(
      functionDeclaration.getReturnType(),
      depth + 1
    )}`;
  }

  private describeClass(
    classDeclaration: ClassDeclaration,
    depth: number
  ): string {
    if (depth > this.maxDepth) {
      return "";
    }
    const indent = "  ".repeat(depth);
    return `${indent}class ${classDeclaration.getName()} {
${classDeclaration
  .getProperties()
  .map((property) => this.describeProperty(property, depth + 1))
  .join("\n")}
${classDeclaration
  .getMethods()
  .map((method) =>
    this.describeFunction(method as unknown as FunctionDeclaration, depth + 1)
  )
  .join("\n")}
${indent}}`;
  }

  private describeProperty(
    property: PropertyDeclaration,
    depth: number
  ): string {
    const indent = "  ".repeat(depth);
    return `${indent}  ${property.getName()}: ${this.describeType(
      property.getType(),
      depth + 1
    )}`;
  }

  private describeInterface(
    interfaceDeclaration: InterfaceDeclaration,
    depth: number
  ): string {
    if (depth > this.maxDepth) {
      return "";
    }
    const indent = "  ".repeat(depth);
    return `${indent}interface ${interfaceDeclaration.getName()} {
${interfaceDeclaration
  .getProperties()
  .map((property) =>
    this.describeProperty(property as unknown as PropertyDeclaration, depth + 1)
  )
  .join("\n")}
${interfaceDeclaration
  .getMethods()
  .map((method) =>
    this.describeFunction(method as unknown as FunctionDeclaration, depth + 1)
  )
  .join("\n")}
${indent}}`;
  }

  private describeTypeAlias(
    typeAlias: TypeAliasDeclaration,
    depth: number
  ): string {
    if (depth > this.maxDepth) {
      return "";
    }
    const indent = "  ".repeat(depth);
    return `${indent}type ${typeAlias.getName()} = ${this.describeType(
      typeAlias.getType(),
      depth + 1
    )}`;
  }

  private describeEnum(
    enumDeclaration: EnumDeclaration,
    depth: number
  ): string {
    if (depth > this.maxDepth) {
      return "";
    }
    const indent = "  ".repeat(depth);
    return `${indent}enum ${enumDeclaration.getName()} {
${enumDeclaration
  .getMembers()
  .map((member) => `${indent}  ${member.getName()} = ${member.getValue()}`)
  .join(",\n")}
${indent}}`;
  }

  private describeType(type: Type, depth: number): string {
    if (depth > this.maxDepth) {
      return "...";
    }
    const indent = "  ".repeat(depth);

    if (type.isUnion()) {
      return type
        .getUnionTypes()
        .map((t) => this.describeType(t, depth))
        .join(" | ");
    }

    if (type.isIntersection()) {
      return type
        .getIntersectionTypes()
        .map((t) => this.describeType(t, depth))
        .join(" & ");
    }

    if (type.isArray()) {
      return `${this.describeType(type.getArrayElementType()!, depth)}[]`;
    }

    if (type.isObject() && !type.isInterface()) {
      const properties = type.getProperties();
      if (properties.length === 0) {
        return "{}";
      }
      return `{
${properties
  .map((prop) => {
    const valueDeclaration = prop.getValueDeclaration();
    if (!valueDeclaration) {
      return `${indent}  ${prop.getName()}: unknown`;
    }
    return `${indent}  ${prop.getName()}: ${this.describeType(
      prop.getTypeAtLocation(valueDeclaration),
      depth + 1
    )}`;
  })
  .join(",\n")}
${indent}}`;
    }

    return type.getText();
  }
}

function getTypeDescriptor(
  identifier: string,
  filePath: string,
  maxDepth: number
): string {
  return new TypeInfo(maxDepth).describe(identifier, filePath);
}

function main() {
  const args = process.argv.slice(2);
  let maxDepth = 5;
  let filePath, identifier;

  for (let i = 0; i < args.length; i++) {
    if (args[i].startsWith("--max-depth=")) {
      maxDepth = parseInt(args[i].split("=")[1], 10);
      if (isNaN(maxDepth)) {
        console.error("Invalid max depth value");
        process.exit(1);
      }
    } else if (!filePath) {
      filePath = args[i];
    } else if (!identifier) {
      identifier = args[i];
    }
  }

  if (!filePath || !identifier) {
    console.error(
      "Usage: node script.js <file_path> <identifier> [--max-depth=<number>]"
    );
    process.exit(1);
  }

  console.log(
    "Getting type info for",
    identifier,
    "in",
    filePath,
    "with max depth",
    maxDepth
  );
  const typeString = getTypeDescriptor(identifier, filePath, maxDepth);

  const outputPath = path.join(process.cwd(), "temp_output_declaration.txt");

  try {
    fs.writeFileSync(outputPath, typeString, "utf8");
    console.log(`Type information has been written to ${outputPath}`);
  } catch (error) {
    console.error(`Error writing to file: ${error}`);
  }
}

main();
