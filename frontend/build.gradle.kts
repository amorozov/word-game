plugins {
    id("org.siouan.frontend-jdk11")
}

group = "com.github.amorozov"
version = "1.0-SNAPSHOT"

frontend {
    nodeDistributionProvided.set(false)
    nodeVersion.set("16.13.1") // the current LTS. It would be nice if we could move it to versions.properties
}
