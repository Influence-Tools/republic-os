---
type: Jurisdiction
title: "Allegany County, MD"
classification: county
fips: "24001"
state: "MD"
demographics:
  population: 67452
  population_under_18: 12032
  population_18_64: 41158
  population_65_plus: 14262
  median_household_income: 59603
  poverty_rate: 16.85
  homeownership_rate: 70.71
  unemployment_rate: 4.99
  median_home_value: 154900
  gini_index: 0.4389
  vacancy_rate: 16.31
  race_white: 58427
  race_black: 4633
  race_asian: 708
  race_native: 155
  hispanic: 1328
  bachelors_plus: 14521
districts:
  - to: "us/states/md/districts/06"
    rel: in-district
    area_weight: 0.9976
  - to: "us/states/md/districts/senate/1"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/md/districts/house/1c"
    rel: in-district
    area_weight: 0.5522
  - to: "us/states/md/districts/house/1b"
    rel: in-district
    area_weight: 0.2684
  - to: "us/states/md/districts/house/1a"
    rel: in-district
    area_weight: 0.1779
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Allegany County, MD

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 67452 |
| Under 18 | 12032 |
| 18–64 | 41158 |
| 65+ | 14262 |
| Median household income | 59603 |
| Poverty rate | 16.85 |
| Homeownership rate | 70.71 |
| Unemployment rate | 4.99 |
| Median home value | 154900 |
| Gini index | 0.4389 |
| Vacancy rate | 16.31 |
| White | 58427 |
| Black | 4633 |
| Asian | 708 |
| Native | 155 |
| Hispanic/Latino | 1328 |
| Bachelor's or higher | 14521 |

## Districts

- [MD-06](/us/states/md/districts/06.md) — 100% (congressional)
- [MD Senate District 1](/us/states/md/districts/senate/1.md) — 100% (state senate)
- [MD House District 1C](/us/states/md/districts/house/1c.md) — 55% (state house)
- [MD House District 1B](/us/states/md/districts/house/1b.md) — 27% (state house)
- [MD House District 1A](/us/states/md/districts/house/1a.md) — 18% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
