---
type: Jurisdiction
title: "Wayne County, OH"
classification: county
fips: "39169"
state: "OH"
demographics:
  population: 116588
  population_under_18: 27936
  population_18_64: 66466
  population_65_plus: 22186
  median_household_income: 73574
  poverty_rate: 9.41
  homeownership_rate: 76.56
  unemployment_rate: 3.3
  median_home_value: 222100
  gini_index: 0.4158
  vacancy_rate: 5.51
  race_white: 108807
  race_black: 1406
  race_asian: 1341
  race_native: 105
  hispanic: 2885
  bachelors_plus: 26570
districts:
  - to: "us/states/oh/districts/07"
    rel: in-district
    area_weight: 0.9996
  - to: "us/states/oh/districts/senate/31"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/house/77"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Wayne County, OH

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 116588 |
| Under 18 | 27936 |
| 18–64 | 66466 |
| 65+ | 22186 |
| Median household income | 73574 |
| Poverty rate | 9.41 |
| Homeownership rate | 76.56 |
| Unemployment rate | 3.3 |
| Median home value | 222100 |
| Gini index | 0.4158 |
| Vacancy rate | 5.51 |
| White | 108807 |
| Black | 1406 |
| Asian | 1341 |
| Native | 105 |
| Hispanic/Latino | 2885 |
| Bachelor's or higher | 26570 |

## Districts

- [OH-07](/us/states/oh/districts/07.md) — 100% (congressional)
- [OH Senate District 31](/us/states/oh/districts/senate/31.md) — 100% (state senate)
- [OH House District 77](/us/states/oh/districts/house/77.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
