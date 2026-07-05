---
type: Jurisdiction
title: "Warren County, IL"
classification: county
fips: "17187"
state: "IL"
demographics:
  population: 16447
  population_under_18: 3693
  population_18_64: 9468
  population_65_plus: 3286
  median_household_income: 67385
  poverty_rate: 14.63
  homeownership_rate: 75.16
  unemployment_rate: 3.59
  median_home_value: 105000
  gini_index: 0.4299
  vacancy_rate: 10.54
  race_white: 13624
  race_black: 438
  race_asian: 395
  race_native: 157
  hispanic: 1820
  bachelors_plus: 3208
districts:
  - to: "us/states/il/districts/15"
    rel: in-district
    area_weight: 0.7338
  - to: "us/states/il/districts/17"
    rel: in-district
    area_weight: 0.2662
  - to: "us/states/il/districts/senate/36"
    rel: in-district
    area_weight: 0.6635
  - to: "us/states/il/districts/senate/47"
    rel: in-district
    area_weight: 0.3365
  - to: "us/states/il/districts/house/71"
    rel: in-district
    area_weight: 0.6635
  - to: "us/states/il/districts/house/94"
    rel: in-district
    area_weight: 0.3365
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, il]
timestamp: "2026-07-03"
---

# Warren County, IL

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 16447 |
| Under 18 | 3693 |
| 18–64 | 9468 |
| 65+ | 3286 |
| Median household income | 67385 |
| Poverty rate | 14.63 |
| Homeownership rate | 75.16 |
| Unemployment rate | 3.59 |
| Median home value | 105000 |
| Gini index | 0.4299 |
| Vacancy rate | 10.54 |
| White | 13624 |
| Black | 438 |
| Asian | 395 |
| Native | 157 |
| Hispanic/Latino | 1820 |
| Bachelor's or higher | 3208 |

## Districts

- [IL-15](/us/states/il/districts/15.md) — 73% (congressional)
- [IL-17](/us/states/il/districts/17.md) — 27% (congressional)
- [IL Senate District 36](/us/states/il/districts/senate/36.md) — 66% (state senate)
- [IL Senate District 47](/us/states/il/districts/senate/47.md) — 34% (state senate)
- [IL House District 71](/us/states/il/districts/house/71.md) — 66% (state house)
- [IL House District 94](/us/states/il/districts/house/94.md) — 34% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
