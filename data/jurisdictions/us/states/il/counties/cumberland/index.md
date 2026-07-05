---
type: Jurisdiction
title: "Cumberland County, IL"
classification: county
fips: "17035"
state: "IL"
demographics:
  population: 10334
  population_under_18: 2317
  population_18_64: 5844
  population_65_plus: 2173
  median_household_income: 73327
  poverty_rate: 9.09
  homeownership_rate: 84.15
  unemployment_rate: 1.35
  median_home_value: 126000
  gini_index: 0.4014
  vacancy_rate: 11.62
  race_white: 9817
  race_black: 18
  race_asian: 4
  race_native: 0
  hispanic: 38
  bachelors_plus: 1874
districts:
  - to: "us/states/il/districts/12"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/il/districts/senate/51"
    rel: in-district
    area_weight: 0.8596
  - to: "us/states/il/districts/senate/54"
    rel: in-district
    area_weight: 0.1404
  - to: "us/states/il/districts/house/102"
    rel: in-district
    area_weight: 0.8595
  - to: "us/states/il/districts/house/107"
    rel: in-district
    area_weight: 0.1404
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Cumberland County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 10334 |
| Under 18 | 2317 |
| 18–64 | 5844 |
| 65+ | 2173 |
| Median household income | 73327 |
| Poverty rate | 9.09 |
| Homeownership rate | 84.15 |
| Unemployment rate | 1.35 |
| Median home value | 126000 |
| Gini index | 0.4014 |
| Vacancy rate | 11.62 |
| White | 9817 |
| Black | 18 |
| Asian | 4 |
| Native | 0 |
| Hispanic/Latino | 38 |
| Bachelor's or higher | 1874 |

## Districts

- [IL-12](/us/states/il/districts/12.md) — 100% (congressional)
- [IL Senate District 51](/us/states/il/districts/senate/51.md) — 86% (state senate)
- [IL Senate District 54](/us/states/il/districts/senate/54.md) — 14% (state senate)
- [IL House District 102](/us/states/il/districts/house/102.md) — 86% (state house)
- [IL House District 107](/us/states/il/districts/house/107.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
