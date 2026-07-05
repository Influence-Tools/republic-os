---
type: Jurisdiction
title: "Orange County, NC"
classification: county
fips: "37135"
state: "NC"
demographics:
  population: 149678
  population_under_18: 28235
  population_18_64: 97346
  population_65_plus: 24097
  median_household_income: 90089
  poverty_rate: 12.48
  homeownership_rate: 63.84
  unemployment_rate: 3.64
  median_home_value: 459500
  gini_index: 0.5142
  vacancy_rate: 8.78
  race_white: 102595
  race_black: 15708
  race_asian: 11806
  race_native: 775
  hispanic: 15914
  bachelors_plus: 90959
districts:
  - to: "us/states/nc/districts/04"
    rel: in-district
    area_weight: 0.9994
  - to: "us/states/nc/districts/senate/23"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nc/districts/house/50"
    rel: in-district
    area_weight: 0.8602
  - to: "us/states/nc/districts/house/56"
    rel: in-district
    area_weight: 0.1397
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Orange County, NC

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 149678 |
| Under 18 | 28235 |
| 18–64 | 97346 |
| 65+ | 24097 |
| Median household income | 90089 |
| Poverty rate | 12.48 |
| Homeownership rate | 63.84 |
| Unemployment rate | 3.64 |
| Median home value | 459500 |
| Gini index | 0.5142 |
| Vacancy rate | 8.78 |
| White | 102595 |
| Black | 15708 |
| Asian | 11806 |
| Native | 775 |
| Hispanic/Latino | 15914 |
| Bachelor's or higher | 90959 |

## Districts

- [NC-04](/us/states/nc/districts/04.md) — 100% (congressional)
- [NC Senate District 23](/us/states/nc/districts/senate/23.md) — 100% (state senate)
- [NC House District 50](/us/states/nc/districts/house/50.md) — 86% (state house)
- [NC House District 56](/us/states/nc/districts/house/56.md) — 14% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
