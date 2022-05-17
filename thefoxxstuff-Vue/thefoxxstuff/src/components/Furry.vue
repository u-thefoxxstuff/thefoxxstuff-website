<template>
    <li>
        {{fur.id}}) {{fur.title}}
    </li>
</template>

<script>
export default {
    props: {
        fur: {
            type: Object,
            required: true
        }
    }
}
</script>