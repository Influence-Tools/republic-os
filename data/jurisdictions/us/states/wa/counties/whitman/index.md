---
type: Jurisdiction
title: "Whitman County, WA"
classification: county
fips: "53075"
state: "WA"
demographics:
  population: 47003
  population_under_18: 7439
  population_18_64: 33967
  population_65_plus: 5597
  median_household_income: 55406
  poverty_rate: 22.66
  homeownership_rate: 46.82
  unemployment_rate: 6.98
  median_home_value: 359600
  gini_index: 0.5205
  vacancy_rate: 15.26
  race_white: 35796
  race_black: 685
  race_asian: 3228
  race_native: 298
  hispanic: 3827
  bachelors_plus: 17728
districts:
  - to: "us/states/wa/districts/05"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wa/districts/senate/9"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/wa/districts/house/9"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Whitman County, WA

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 47003 |
| Under 18 | 7439 |
| 18–64 | 33967 |
| 65+ | 5597 |
| Median household income | 55406 |
| Poverty rate | 22.66 |
| Homeownership rate | 46.82 |
| Unemployment rate | 6.98 |
| Median home value | 359600 |
| Gini index | 0.5205 |
| Vacancy rate | 15.26 |
| White | 35796 |
| Black | 685 |
| Asian | 3228 |
| Native | 298 |
| Hispanic/Latino | 3827 |
| Bachelor's or higher | 17728 |

## Districts

- [WA-05](/us/states/wa/districts/05.md) — 100% (congressional)
- [WA Senate District 9](/us/states/wa/districts/senate/9.md) — 100% (state senate)
- [WA House District 9](/us/states/wa/districts/house/9.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
