---
type: Jurisdiction
title: "Mahoning County, OH"
classification: county
fips: "39099"
state: "OH"
demographics:
  population: 226491
  population_under_18: 45920
  population_18_64: 129675
  population_65_plus: 50896
  median_household_income: 56942
  poverty_rate: 18.9
  homeownership_rate: 70.26
  unemployment_rate: 6.38
  median_home_value: 154700
  gini_index: 0.4782
  vacancy_rate: 9.19
  race_white: 169668
  race_black: 31660
  race_asian: 1869
  race_native: 435
  hispanic: 15428
  bachelors_plus: 59554
districts:
  - to: "us/states/oh/districts/06"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/senate/33"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/house/59"
    rel: in-district
    area_weight: 0.6565
  - to: "us/states/oh/districts/house/58"
    rel: in-district
    area_weight: 0.3433
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Mahoning County, OH

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 226491 |
| Under 18 | 45920 |
| 18–64 | 129675 |
| 65+ | 50896 |
| Median household income | 56942 |
| Poverty rate | 18.9 |
| Homeownership rate | 70.26 |
| Unemployment rate | 6.38 |
| Median home value | 154700 |
| Gini index | 0.4782 |
| Vacancy rate | 9.19 |
| White | 169668 |
| Black | 31660 |
| Asian | 1869 |
| Native | 435 |
| Hispanic/Latino | 15428 |
| Bachelor's or higher | 59554 |

## Districts

- [OH-06](/us/states/oh/districts/06.md) — 100% (congressional)
- [OH Senate District 33](/us/states/oh/districts/senate/33.md) — 100% (state senate)
- [OH House District 59](/us/states/oh/districts/house/59.md) — 66% (state house)
- [OH House District 58](/us/states/oh/districts/house/58.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
