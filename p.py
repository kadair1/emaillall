import replicate
output = replicate.run(
    "elizabethsiegle/agihouse-sf-rip:ea8c1f072009cdf0700acae2a45a81f0039ba5cd7c2d121d9c8de6d7308a6fe0",
    input={"prompt": "<subject>Meeting time?<subject>"}
)
print(output)