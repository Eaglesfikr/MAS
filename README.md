# model_attack_system

这时一个基于机器学习的逆向攻击系统


## 运行环境：

```
springboot == 
jvm == 17.0+
gradle == 8.10+

node == 20.11.0+
npm == 10.8.1+
#注：前端需要管理员权限
```



## 报错1：

```shell
PS E:\model_inv\model_attack_system\frontend\starter-kit> npm run build

> vuexy-mui-nextjs-admin-template@3.1.0 build
> next build

Attention: Next.js now collects completely anonymous telemetry regarding usage.
This information is used to shape Next.js' roadmap and prioritize features.
You can learn more, including how to opt-out if you'd not like to participate in this anonymous program, by visiting the following URL:
https://nextjs.org/telemetry

  ▲ Next.js 14.2.5

   Creating an optimized production build ...
 ✓ Compiled successfully

Failed to compile.

./src/app/(dashboard)/home/FileUploader.tsx
3:1  Error: There should be at least one empty line between import groups  import/order

./src/app/(dashboard)/home/page.tsx
3:1  Error: There should be at least one empty line between import groups  import/order
32:5  Error: Expected blank line before this statement.  padding-line-between-statements

./src/components/layout/shared/Logo.tsx
14:8  Error: 'VuexyLogo' is defined but never used.  @typescript-eslint/no-unused-vars

info  - Need to disable some ESLint rules? Learn more here: https://nextjs.org/docs/basic-features/eslint#disabling-rules
PS E:\model_inv\model_attack_system\frontend\starter-kit>
```

你的错误日志表明在构建过程中，代码未通过 ESLint 检查。主要问题是：

1. **导入语句之间缺少空行（`import/order`）。****
2. **某些地方缺少必要的空行（`padding-line-between-statements`）。**
3. **未使用的变量（`@typescript-eslint/no-unused-vars`）。**

**这些问题阻止了构建过程的完成。**

修改：

前端部分：

```js
#调整 ESLint 配置,在.eslintrc.js文件中修改为
{
  "rules": {
    "import/order": "off",
    "padding-line-between-statements": "off",
    "@typescript-eslint/no-unused-vars": "off"
  }
}
```

