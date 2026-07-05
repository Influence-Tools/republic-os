---
type: Jurisdiction
title: "Williamson County, TX"
classification: county
fips: "48491"
state: "TX"
demographics:
  population: 672688
  population_under_18: 161946
  population_18_64: 423834
  population_65_plus: 86908
  median_household_income: 111340
  poverty_rate: 6.43
  homeownership_rate: 66.4
  unemployment_rate: 3.88
  median_home_value: 447000
  gini_index: 0.4155
  vacancy_rate: 3.93
  race_white: 400958
  race_black: 46889
  race_asian: 67402
  race_native: 2935
  hispanic: 166454
  bachelors_plus: 303533
districts:
  - to: "us/states/tx/districts/31"
    rel: in-district
    area_weight: 0.7816
  - to: "us/states/tx/districts/17"
    rel: in-district
    area_weight: 0.1867
  - to: "us/states/tx/districts/10"
    rel: in-district
    area_weight: 0.0175
  - to: "us/states/tx/districts/37"
    rel: in-district
    area_weight: 0.0142
  - to: "us/states/tx/districts/senate/5"
    rel: in-district
    area_weight: 0.9007
  - to: "us/states/tx/districts/senate/24"
    rel: in-district
    area_weight: 0.0992
  - to: "us/states/tx/districts/house/52"
    rel: in-district
    area_weight: 0.6081
  - to: "us/states/tx/districts/house/20"
    rel: in-district
    area_weight: 0.3396
  - to: "us/states/tx/districts/house/136"
    rel: in-district
    area_weight: 0.0522
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Williamson County, TX

County jurisdiction — 5 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 672688 |
| Under 18 | 161946 |
| 18–64 | 423834 |
| 65+ | 86908 |
| Median household income | 111340 |
| Poverty rate | 6.43 |
| Homeownership rate | 66.4 |
| Unemployment rate | 3.88 |
| Median home value | 447000 |
| Gini index | 0.4155 |
| Vacancy rate | 3.93 |
| White | 400958 |
| Black | 46889 |
| Asian | 67402 |
| Native | 2935 |
| Hispanic/Latino | 166454 |
| Bachelor's or higher | 303533 |

## Districts

- [TX-31](/us/states/tx/districts/31.md) — 78% (congressional)
- [TX-17](/us/states/tx/districts/17.md) — 19% (congressional)
- [TX-10](/us/states/tx/districts/10.md) — 2% (congressional)
- [TX-37](/us/states/tx/districts/37.md) — 1% (congressional)
- [TX Senate District 5](/us/states/tx/districts/senate/5.md) — 90% (state senate)
- [TX Senate District 24](/us/states/tx/districts/senate/24.md) — 10% (state senate)
- [TX House District 52](/us/states/tx/districts/house/52.md) — 61% (state house)
- [TX House District 20](/us/states/tx/districts/house/20.md) — 34% (state house)
- [TX House District 136](/us/states/tx/districts/house/136.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
