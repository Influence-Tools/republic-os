---
type: Jurisdiction
title: "Delaware County, OH"
classification: county
fips: "39041"
state: "OH"
demographics:
  population: 226834
  population_under_18: 56264
  population_18_64: 136405
  population_65_plus: 34165
  median_household_income: 133540
  poverty_rate: 4.67
  homeownership_rate: 78.51
  unemployment_rate: 2.97
  median_home_value: 445500
  gini_index: 0.4191
  vacancy_rate: 4.62
  race_white: 181317
  race_black: 9931
  race_asian: 19485
  race_native: 139
  hispanic: 7899
  bachelors_plus: 126879
districts:
  - to: "us/states/oh/districts/04"
    rel: in-district
    area_weight: 0.6743
  - to: "us/states/oh/districts/12"
    rel: in-district
    area_weight: 0.3256
  - to: "us/states/oh/districts/senate/19"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/61"
    rel: in-district
    area_weight: 0.6809
  - to: "us/states/oh/districts/house/60"
    rel: in-district
    area_weight: 0.3189
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Delaware County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 226834 |
| Under 18 | 56264 |
| 18–64 | 136405 |
| 65+ | 34165 |
| Median household income | 133540 |
| Poverty rate | 4.67 |
| Homeownership rate | 78.51 |
| Unemployment rate | 2.97 |
| Median home value | 445500 |
| Gini index | 0.4191 |
| Vacancy rate | 4.62 |
| White | 181317 |
| Black | 9931 |
| Asian | 19485 |
| Native | 139 |
| Hispanic/Latino | 7899 |
| Bachelor's or higher | 126879 |

## Districts

- [OH-04](/us/states/oh/districts/04.md) — 67% (congressional)
- [OH-12](/us/states/oh/districts/12.md) — 33% (congressional)
- [OH Senate District 19](/us/states/oh/districts/senate/19.md) — 100% (state senate)
- [OH House District 61](/us/states/oh/districts/house/61.md) — 68% (state house)
- [OH House District 60](/us/states/oh/districts/house/60.md) — 32% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
