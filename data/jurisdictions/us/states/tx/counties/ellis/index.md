---
type: Jurisdiction
title: "Ellis County, TX"
classification: county
fips: "48139"
state: "TX"
demographics:
  population: 213160
  population_under_18: 56170
  population_18_64: 129202
  population_65_plus: 27788
  median_household_income: 99595
  poverty_rate: 6.9
  homeownership_rate: 75.79
  unemployment_rate: 4.46
  median_home_value: 348600
  gini_index: 0.3976
  vacancy_rate: 4.86
  race_white: 126957
  race_black: 30976
  race_asian: 1820
  race_native: 1111
  hispanic: 60062
  bachelors_plus: 55591
districts:
  - to: "us/states/tx/districts/06"
    rel: in-district
    area_weight: 0.9982
  - to: "us/states/tx/districts/senate/2"
    rel: in-district
    area_weight: 0.5944
  - to: "us/states/tx/districts/senate/22"
    rel: in-district
    area_weight: 0.4056
  - to: "us/states/tx/districts/house/10"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Ellis County, TX

County jurisdiction — 6 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 213160 |
| Under 18 | 56170 |
| 18–64 | 129202 |
| 65+ | 27788 |
| Median household income | 99595 |
| Poverty rate | 6.9 |
| Homeownership rate | 75.79 |
| Unemployment rate | 4.46 |
| Median home value | 348600 |
| Gini index | 0.3976 |
| Vacancy rate | 4.86 |
| White | 126957 |
| Black | 30976 |
| Asian | 1820 |
| Native | 1111 |
| Hispanic/Latino | 60062 |
| Bachelor's or higher | 55591 |

## Districts

- [TX-06](/us/states/tx/districts/06.md) — 100% (congressional)
- [TX Senate District 2](/us/states/tx/districts/senate/2.md) — 59% (state senate)
- [TX Senate District 22](/us/states/tx/districts/senate/22.md) — 41% (state senate)
- [TX House District 10](/us/states/tx/districts/house/10.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
