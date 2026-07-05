---
type: Jurisdiction
title: "Lorain County, OH"
classification: county
fips: "39093"
state: "OH"
demographics:
  population: 317129
  population_under_18: 68331
  population_18_64: 185896
  population_65_plus: 62902
  median_household_income: 73347
  poverty_rate: 12.09
  homeownership_rate: 74.02
  unemployment_rate: 4.3
  median_home_value: 223200
  gini_index: 0.4627
  vacancy_rate: 6.59
  race_white: 247434
  race_black: 24301
  race_asian: 4481
  race_native: 494
  hispanic: 35037
  bachelors_plus: 87529
districts:
  - to: "us/states/oh/districts/05"
    rel: in-district
    area_weight: 0.5343
  - to: "us/states/oh/districts/senate/13"
    rel: in-district
    area_weight: 0.5342
  - to: "us/states/oh/districts/house/54"
    rel: in-district
    area_weight: 0.3792
  - to: "us/states/oh/districts/house/52"
    rel: in-district
    area_weight: 0.0932
  - to: "us/states/oh/districts/house/53"
    rel: in-district
    area_weight: 0.0618
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Lorain County, OH

County jurisdiction — 7 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 317129 |
| Under 18 | 68331 |
| 18–64 | 185896 |
| 65+ | 62902 |
| Median household income | 73347 |
| Poverty rate | 12.09 |
| Homeownership rate | 74.02 |
| Unemployment rate | 4.3 |
| Median home value | 223200 |
| Gini index | 0.4627 |
| Vacancy rate | 6.59 |
| White | 247434 |
| Black | 24301 |
| Asian | 4481 |
| Native | 494 |
| Hispanic/Latino | 35037 |
| Bachelor's or higher | 87529 |

## Districts

- [OH-05](/us/states/oh/districts/05.md) — 53% (congressional)
- [OH Senate District 13](/us/states/oh/districts/senate/13.md) — 53% (state senate)
- [OH House District 54](/us/states/oh/districts/house/54.md) — 38% (state house)
- [OH House District 52](/us/states/oh/districts/house/52.md) — 9% (state house)
- [OH House District 53](/us/states/oh/districts/house/53.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
