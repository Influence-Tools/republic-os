---
type: Jurisdiction
title: "Union County, SC"
classification: county
fips: "45087"
state: "SC"
demographics:
  population: 26885
  population_under_18: 5590
  population_18_64: 15485
  population_65_plus: 5810
  median_household_income: 41621
  poverty_rate: 22.62
  homeownership_rate: 71.28
  unemployment_rate: 7.94
  median_home_value: 103600
  gini_index: 0.4691
  vacancy_rate: 14.16
  race_white: 17346
  race_black: 7475
  race_asian: 43
  race_native: 81
  hispanic: 559
  bachelors_plus: 3601
districts:
  - to: "us/states/sc/districts/05"
    rel: in-district
    area_weight: 0.9965
  - to: "us/states/sc/districts/senate/13"
    rel: in-district
    area_weight: 0.4094
  - to: "us/states/sc/districts/senate/9"
    rel: in-district
    area_weight: 0.3957
  - to: "us/states/sc/districts/senate/14"
    rel: in-district
    area_weight: 0.1948
  - to: "us/states/sc/districts/house/42"
    rel: in-district
    area_weight: 0.9997
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, sc]
timestamp: "2026-07-03"
---

# Union County, SC

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 26885 |
| Under 18 | 5590 |
| 18–64 | 15485 |
| 65+ | 5810 |
| Median household income | 41621 |
| Poverty rate | 22.62 |
| Homeownership rate | 71.28 |
| Unemployment rate | 7.94 |
| Median home value | 103600 |
| Gini index | 0.4691 |
| Vacancy rate | 14.16 |
| White | 17346 |
| Black | 7475 |
| Asian | 43 |
| Native | 81 |
| Hispanic/Latino | 559 |
| Bachelor's or higher | 3601 |

## Districts

- [SC-05](/us/states/sc/districts/05.md) — 100% (congressional)
- [SC Senate District 13](/us/states/sc/districts/senate/13.md) — 41% (state senate)
- [SC Senate District 9](/us/states/sc/districts/senate/9.md) — 40% (state senate)
- [SC Senate District 14](/us/states/sc/districts/senate/14.md) — 19% (state senate)
- [SC House District 42](/us/states/sc/districts/house/42.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
