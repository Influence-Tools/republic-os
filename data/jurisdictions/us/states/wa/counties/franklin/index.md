---
type: Jurisdiction
title: "Franklin County, WA"
classification: county
fips: "53021"
state: "WA"
demographics:
  population: 98902
  population_under_18: 30565
  population_18_64: 58080
  population_65_plus: 10257
  median_household_income: 86714
  poverty_rate: 13.13
  homeownership_rate: 70.96
  unemployment_rate: 5.43
  median_home_value: 379300
  gini_index: 0.4242
  vacancy_rate: 4.15
  race_white: 44953
  race_black: 1909
  race_asian: 1825
  race_native: 1342
  hispanic: 54664
  bachelors_plus: 16765
districts:
  - to: "us/states/wa/districts/05"
    rel: in-district
    area_weight: 0.8986
  - to: "us/states/wa/districts/04"
    rel: in-district
    area_weight: 0.1014
  - to: "us/states/wa/districts/senate/16"
    rel: in-district
    area_weight: 0.9825
  - to: "us/states/wa/districts/senate/14"
    rel: in-district
    area_weight: 0.0093
  - to: "us/states/wa/districts/senate/8"
    rel: in-district
    area_weight: 0.0079
  - to: "us/states/wa/districts/house/16"
    rel: in-district
    area_weight: 0.9825
  - to: "us/states/wa/districts/house/14"
    rel: in-district
    area_weight: 0.0093
  - to: "us/states/wa/districts/house/8"
    rel: in-district
    area_weight: 0.0079
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wa]
timestamp: "2026-07-03"
---

# Franklin County, WA

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 98902 |
| Under 18 | 30565 |
| 18–64 | 58080 |
| 65+ | 10257 |
| Median household income | 86714 |
| Poverty rate | 13.13 |
| Homeownership rate | 70.96 |
| Unemployment rate | 5.43 |
| Median home value | 379300 |
| Gini index | 0.4242 |
| Vacancy rate | 4.15 |
| White | 44953 |
| Black | 1909 |
| Asian | 1825 |
| Native | 1342 |
| Hispanic/Latino | 54664 |
| Bachelor's or higher | 16765 |

## Districts

- [WA-05](/us/states/wa/districts/05.md) — 90% (congressional)
- [WA-04](/us/states/wa/districts/04.md) — 10% (congressional)
- [WA Senate District 16](/us/states/wa/districts/senate/16.md) — 98% (state senate)
- [WA Senate District 14](/us/states/wa/districts/senate/14.md) — 1% (state senate)
- [WA Senate District 8](/us/states/wa/districts/senate/8.md) — 1% (state senate)
- [WA House District 16](/us/states/wa/districts/house/16.md) — 98% (state house)
- [WA House District 14](/us/states/wa/districts/house/14.md) — 1% (state house)
- [WA House District 8](/us/states/wa/districts/house/8.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
