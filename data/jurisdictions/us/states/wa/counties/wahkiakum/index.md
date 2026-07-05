---
type: Jurisdiction
title: "Wahkiakum County, WA"
classification: county
fips: "53069"
state: "WA"
demographics:
  population: 4658
  population_under_18: 817
  population_18_64: 2251
  population_65_plus: 1590
  median_household_income: 62653
  poverty_rate: 17.82
  homeownership_rate: 83.19
  unemployment_rate: 3.48
  median_home_value: 396800
  gini_index: 0.4787
  vacancy_rate: 6.67
  race_white: 4084
  race_black: 39
  race_asian: 78
  race_native: 10
  hispanic: 261
  bachelors_plus: 1077
districts:
  - to: "us/states/wa/districts/03"
    rel: in-district
    area_weight: 0.9637
  - to: "us/states/wa/districts/senate/19"
    rel: in-district
    area_weight: 0.9646
  - to: "us/states/wa/districts/house/19"
    rel: in-district
    area_weight: 0.9646
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Wahkiakum County, WA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4658 |
| Under 18 | 817 |
| 18–64 | 2251 |
| 65+ | 1590 |
| Median household income | 62653 |
| Poverty rate | 17.82 |
| Homeownership rate | 83.19 |
| Unemployment rate | 3.48 |
| Median home value | 396800 |
| Gini index | 0.4787 |
| Vacancy rate | 6.67 |
| White | 4084 |
| Black | 39 |
| Asian | 78 |
| Native | 10 |
| Hispanic/Latino | 261 |
| Bachelor's or higher | 1077 |

## Districts

- [WA-03](/us/states/wa/districts/03.md) — 96% (congressional)
- [WA Senate District 19](/us/states/wa/districts/senate/19.md) — 96% (state senate)
- [WA House District 19](/us/states/wa/districts/house/19.md) — 96% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
