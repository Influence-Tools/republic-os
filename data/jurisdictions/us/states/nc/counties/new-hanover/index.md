---
type: Jurisdiction
title: "New Hanover County, NC"
classification: county
fips: "37129"
state: "NC"
demographics:
  population: 235229
  population_under_18: 42122
  population_18_64: 148297
  population_65_plus: 44810
  median_household_income: 75166
  poverty_rate: 12.29
  homeownership_rate: 61.4
  unemployment_rate: 4.49
  median_home_value: 387800
  gini_index: 0.4816
  vacancy_rate: 12.66
  race_white: 180170
  race_black: 25672
  race_asian: 3250
  race_native: 405
  hispanic: 18547
  bachelors_plus: 100756
districts:
  - to: "us/states/nc/districts/07"
    rel: in-district
    area_weight: 0.6638
  - to: "us/states/nc/districts/senate/7"
    rel: in-district
    area_weight: 0.6363
  - to: "us/states/nc/districts/senate/8"
    rel: in-district
    area_weight: 0.0306
  - to: "us/states/nc/districts/house/20"
    rel: in-district
    area_weight: 0.4082
  - to: "us/states/nc/districts/house/19"
    rel: in-district
    area_weight: 0.1371
  - to: "us/states/nc/districts/house/18"
    rel: in-district
    area_weight: 0.1215
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# New Hanover County, NC

County jurisdiction — 4 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 235229 |
| Under 18 | 42122 |
| 18–64 | 148297 |
| 65+ | 44810 |
| Median household income | 75166 |
| Poverty rate | 12.29 |
| Homeownership rate | 61.4 |
| Unemployment rate | 4.49 |
| Median home value | 387800 |
| Gini index | 0.4816 |
| Vacancy rate | 12.66 |
| White | 180170 |
| Black | 25672 |
| Asian | 3250 |
| Native | 405 |
| Hispanic/Latino | 18547 |
| Bachelor's or higher | 100756 |

## Districts

- [NC-07](/us/states/nc/districts/07.md) — 66% (congressional)
- [NC Senate District 7](/us/states/nc/districts/senate/7.md) — 64% (state senate)
- [NC Senate District 8](/us/states/nc/districts/senate/8.md) — 3% (state senate)
- [NC House District 20](/us/states/nc/districts/house/20.md) — 41% (state house)
- [NC House District 19](/us/states/nc/districts/house/19.md) — 14% (state house)
- [NC House District 18](/us/states/nc/districts/house/18.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
