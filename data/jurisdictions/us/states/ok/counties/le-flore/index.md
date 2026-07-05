---
type: Jurisdiction
title: "Le Flore County, OK"
classification: county
fips: "40079"
state: "OK"
demographics:
  population: 49053
  population_under_18: 11953
  population_18_64: 28302
  population_65_plus: 8798
  median_household_income: 51565
  poverty_rate: 19.37
  homeownership_rate: 72.75
  unemployment_rate: 5.21
  median_home_value: 135700
  gini_index: 0.4468
  vacancy_rate: 15.3
  race_white: 34492
  race_black: 866
  race_asian: 367
  race_native: 5613
  hispanic: 3903
  bachelors_plus: 6685
districts:
  - to: "us/states/ok/districts/02"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/ok/districts/senate/5"
    rel: in-district
    area_weight: 0.9693
  - to: "us/states/ok/districts/senate/7"
    rel: in-district
    area_weight: 0.0305
  - to: "us/states/ok/districts/house/1"
    rel: in-district
    area_weight: 0.5366
  - to: "us/states/ok/districts/house/3"
    rel: in-district
    area_weight: 0.3915
  - to: "us/states/ok/districts/house/15"
    rel: in-district
    area_weight: 0.0716
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ok]
timestamp: "2026-07-03"
---

# Le Flore County, OK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 49053 |
| Under 18 | 11953 |
| 18–64 | 28302 |
| 65+ | 8798 |
| Median household income | 51565 |
| Poverty rate | 19.37 |
| Homeownership rate | 72.75 |
| Unemployment rate | 5.21 |
| Median home value | 135700 |
| Gini index | 0.4468 |
| Vacancy rate | 15.3 |
| White | 34492 |
| Black | 866 |
| Asian | 367 |
| Native | 5613 |
| Hispanic/Latino | 3903 |
| Bachelor's or higher | 6685 |

## Districts

- [OK-02](/us/states/ok/districts/02.md) — 100% (congressional)
- [OK Senate District 5](/us/states/ok/districts/senate/5.md) — 97% (state senate)
- [OK Senate District 7](/us/states/ok/districts/senate/7.md) — 3% (state senate)
- [OK House District 1](/us/states/ok/districts/house/1.md) — 54% (state house)
- [OK House District 3](/us/states/ok/districts/house/3.md) — 39% (state house)
- [OK House District 15](/us/states/ok/districts/house/15.md) — 7% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
