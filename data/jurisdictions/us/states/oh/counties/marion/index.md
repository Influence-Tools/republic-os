---
type: Jurisdiction
title: "Marion County, OH"
classification: county
fips: "39101"
state: "OH"
demographics:
  population: 65020
  population_under_18: 13864
  population_18_64: 39016
  population_65_plus: 12140
  median_household_income: 59371
  poverty_rate: 16.65
  homeownership_rate: 67.46
  unemployment_rate: 6.32
  median_home_value: 156800
  gini_index: 0.4444
  vacancy_rate: 9.78
  race_white: 56588
  race_black: 3195
  race_asian: 395
  race_native: 146
  hispanic: 2098
  bachelors_plus: 9080
districts:
  - to: "us/states/oh/districts/04"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/senate/26"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/oh/districts/house/87"
    rel: in-district
    area_weight: 0.7778
  - to: "us/states/oh/districts/house/86"
    rel: in-district
    area_weight: 0.2222
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Marion County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 65020 |
| Under 18 | 13864 |
| 18–64 | 39016 |
| 65+ | 12140 |
| Median household income | 59371 |
| Poverty rate | 16.65 |
| Homeownership rate | 67.46 |
| Unemployment rate | 6.32 |
| Median home value | 156800 |
| Gini index | 0.4444 |
| Vacancy rate | 9.78 |
| White | 56588 |
| Black | 3195 |
| Asian | 395 |
| Native | 146 |
| Hispanic/Latino | 2098 |
| Bachelor's or higher | 9080 |

## Districts

- [OH-04](/us/states/oh/districts/04.md) — 100% (congressional)
- [OH Senate District 26](/us/states/oh/districts/senate/26.md) — 100% (state senate)
- [OH House District 87](/us/states/oh/districts/house/87.md) — 78% (state house)
- [OH House District 86](/us/states/oh/districts/house/86.md) — 22% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
