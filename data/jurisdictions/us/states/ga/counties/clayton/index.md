---
type: Jurisdiction
title: "Clayton County, GA"
classification: county
fips: "13063"
state: "GA"
demographics:
  population: 298924
  population_under_18: 80080
  population_18_64: 186822
  population_65_plus: 32022
  median_household_income: 59806
  poverty_rate: 17.95
  homeownership_rate: 54.54
  unemployment_rate: 7.2
  median_home_value: 222300
  gini_index: 0.4246
  vacancy_rate: 8.26
  race_white: 28917
  race_black: 207482
  race_asian: 14751
  race_native: 1345
  hispanic: 43419
  bachelors_plus: 57176
districts:
  - to: "us/states/ga/districts/13"
    rel: in-district
    area_weight: 0.5325
  - to: "us/states/ga/districts/05"
    rel: in-district
    area_weight: 0.4658
  - to: "us/states/ga/districts/senate/34"
    rel: in-district
    area_weight: 0.4172
  - to: "us/states/ga/districts/senate/17"
    rel: in-district
    area_weight: 0.3823
  - to: "us/states/ga/districts/senate/44"
    rel: in-district
    area_weight: 0.2003
  - to: "us/states/ga/districts/house/74"
    rel: in-district
    area_weight: 0.2438
  - to: "us/states/ga/districts/house/77"
    rel: in-district
    area_weight: 0.2111
  - to: "us/states/ga/districts/house/76"
    rel: in-district
    area_weight: 0.1911
  - to: "us/states/ga/districts/house/75"
    rel: in-district
    area_weight: 0.1666
  - to: "us/states/ga/districts/house/79"
    rel: in-district
    area_weight: 0.1191
  - to: "us/states/ga/districts/house/78"
    rel: in-district
    area_weight: 0.068
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Clayton County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 298924 |
| Under 18 | 80080 |
| 18–64 | 186822 |
| 65+ | 32022 |
| Median household income | 59806 |
| Poverty rate | 17.95 |
| Homeownership rate | 54.54 |
| Unemployment rate | 7.2 |
| Median home value | 222300 |
| Gini index | 0.4246 |
| Vacancy rate | 8.26 |
| White | 28917 |
| Black | 207482 |
| Asian | 14751 |
| Native | 1345 |
| Hispanic/Latino | 43419 |
| Bachelor's or higher | 57176 |

## Districts

- [GA-13](/us/states/ga/districts/13.md) — 53% (congressional)
- [GA-05](/us/states/ga/districts/05.md) — 47% (congressional)
- [GA Senate District 34](/us/states/ga/districts/senate/34.md) — 42% (state senate)
- [GA Senate District 17](/us/states/ga/districts/senate/17.md) — 38% (state senate)
- [GA Senate District 44](/us/states/ga/districts/senate/44.md) — 20% (state senate)
- [GA House District 74](/us/states/ga/districts/house/74.md) — 24% (state house)
- [GA House District 77](/us/states/ga/districts/house/77.md) — 21% (state house)
- [GA House District 76](/us/states/ga/districts/house/76.md) — 19% (state house)
- [GA House District 75](/us/states/ga/districts/house/75.md) — 17% (state house)
- [GA House District 79](/us/states/ga/districts/house/79.md) — 12% (state house)
- [GA House District 78](/us/states/ga/districts/house/78.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
